"""Input handler for interactive prompts"""

import os
from pathlib import Path
from .logger import Logger

class InputHandler:
    """Handles user input and validation"""

    @staticmethod
    def get_target_url() -> str:
        """Get target URL from user"""
        Logger.info("\n[*] Enter target URL")
        Logger.info("    Default: http://10.48.184.96/index.php")
        url = Logger.input_prompt("    Target URL: ").strip()

        if not url:
            url = "http://10.48.184.96/index.php"
            Logger.info(f"    Using default: {url}")

        return url

    @staticmethod
    def get_username() -> str:
        """Get username from user"""
        Logger.info("\n[*] Enter target username")
        Logger.info("    Default: admin")
        username = Logger.input_prompt("    Username: ").strip()

        if not username:
            username = "admin"
            Logger.info(f"    Using default: {username}")

        return username

    @staticmethod
    def get_wordlist_path() -> str:
        """Get wordlist file path from user"""
        Logger.info("\n[*] Enter wordlist file path")
        Logger.info("    Default: /usr/share/wordlists/rockyou.txt")
        Logger.info("    Common paths:")
        Logger.info("      - /usr/share/wordlists/rockyou.txt")
        Logger.info("      - /usr/share/wordlists/common.txt")
        Logger.info("      - ./passwords.txt")

        while True:
            path = Logger.input_prompt("    Wordlist path: ").strip()

            if not path:
                path = "/usr/share/wordlists/rockyou.txt"
                Logger.info(f"    Using default: {path}")

            if os.path.isfile(path):
                Logger.success(f"    ✓ File found: {path}")
                return path
            else:
                Logger.error(f"    ✗ File not found: {path}")
                retry = Logger.input_prompt("    Try another path? (y/n): ").strip().lower()
                if retry != 'y':
                    Logger.warning("    Using default path...")
                    return "/usr/share/wordlists/rockyou.txt"

    @staticmethod
    def get_max_passwords() -> int:
        """Get maximum passwords to try"""
        Logger.info("\n[*] Maximum passwords to try")
        Logger.info("    Default: 100")
        Logger.info("    Examples: 50, 100, 500, 1000")

        while True:
            try:
                max_pwd = Logger.input_prompt("    Max passwords: ").strip()

                if not max_pwd:
                    max_pwd = 100
                    Logger.info(f"    Using default: {max_pwd}")
                    return max_pwd

                max_pwd = int(max_pwd)
                if max_pwd < 1:
                    Logger.error("    ✗ Must be at least 1")
                    continue

                Logger.success(f"    ✓ Set to {max_pwd} passwords")
                return max_pwd

            except ValueError:
                Logger.error("    ✗ Invalid number. Please enter digits only.")

    @staticmethod
    def get_max_workers() -> int:
        """Get number of concurrent workers"""
        Logger.info("\n[*] Number of concurrent workers")
        Logger.info("    Default: 5")
        Logger.info("    Note: More workers = faster but uses more resources")
        Logger.info("    Recommended: 2-8 (based on your system)")

        while True:
            try:
                workers = Logger.input_prompt("    Max workers: ").strip()

                if not workers:
                    workers = 5
                    Logger.info(f"    Using default: {workers}")
                    return workers

                workers = int(workers)
                if workers < 1:
                    Logger.error("    ✗ Must be at least 1")
                    continue
                elif workers > 16:
                    Logger.warning("    ⚠ Warning: More than 16 workers may cause issues")
                    confirm = Logger.input_prompt("    Continue? (y/n): ").strip().lower()
                    if confirm != 'y':
                        continue

                Logger.success(f"    ✓ Set to {workers} workers")
                return workers

            except ValueError:
                Logger.error("    ✗ Invalid number. Please enter digits only.")

    @staticmethod
    def get_ocr_engine() -> str:
        """Get OCR engine choice"""
        Logger.info("\n[*] Select OCR Engine")
        Logger.info("    1 = Pytesseract (lightweight, ~300MB)")
        Logger.info("    2 = EasyOCR (accurate, ~2GB)")
        Logger.info("    Default: 1 (Pytesseract)")

        while True:
            choice = Logger.input_prompt("    Choice (1-2): ").strip()

            if not choice:
                Logger.info("    Using default: Pytesseract")
                return "pytesseract"

            if choice == "1":
                Logger.success("    ✓ Using Pytesseract")
                return "pytesseract"
            elif choice == "2":
                Logger.success("    ✓ Using EasyOCR")
                return "easyocr"
            else:
                Logger.error("    ✗ Invalid choice. Enter 1 or 2")

    @staticmethod
    def get_captcha_strength() -> str:
        """Get CAPTCHA strength/difficulty level"""
        from ..config import CAPTCHA_STRENGTHS

        Logger.info("\n[*] Select CAPTCHA Strength/Difficulty")
        Logger.info("    (Affects OCR accuracy and brute force strategy)")
        Logger.info("")

        for idx, (level, info) in enumerate(CAPTCHA_STRENGTHS.items(), 1):
            Logger.info(f"    {idx} = {level.upper()}")
            Logger.info(f"       {info['description']}")
            Logger.info(f"       Pattern: {info['pattern']}")
            Logger.info(f"       OCR Accuracy: {info['ocr_accuracy']}")
            Logger.info("")

        Logger.info("    Default: 2 (Medium - like J4HUX)")

        while True:
            choice = Logger.input_prompt("    Choice (1-4): ").strip()

            if not choice:
                Logger.info("    Using default: MEDIUM (4-5 chars, letters+numbers)")
                return "medium"

            strength_map = {
                "1": "easy",
                "2": "medium",
                "3": "hard",
                "4": "extreme"
            }

            if choice in strength_map:
                strength = strength_map[choice]
                Logger.success(f"    ✓ Selected: {strength.upper()}")
                return strength
            else:
                Logger.error("    ✗ Invalid choice. Enter 1-4")

    @staticmethod
    def confirm_settings(target_url: str, username: str, wordlist: str, 
                        max_pwd: int, max_workers: int, ocr_engine: str,
                        captcha_strength: str) -> bool:
        """Confirm all settings before starting"""
        from ..config import CAPTCHA_STRENGTHS

        Logger.separator()
        Logger.info("CONFIGURATION SUMMARY")
        Logger.separator()
        Logger.info(f"Target URL:        {target_url}")
        Logger.info(f"Username:          {username}")
        Logger.info(f"Wordlist:          {wordlist}")
        Logger.info(f"Max Passwords:     {max_pwd}")
        Logger.info(f"Max Workers:       {max_workers}")
        Logger.info(f"OCR Engine:        {ocr_engine}")
        Logger.info(f"CAPTCHA Strength:  {captcha_strength.upper()}")

        # Show CAPTCHA details
        if captcha_strength in CAPTCHA_STRENGTHS:
            info = CAPTCHA_STRENGTHS[captcha_strength]
            Logger.info(f"  → {info['description']}")
            Logger.info(f"  → {info['pattern']}")
            Logger.info(f"  → Expected OCR Accuracy: {info['ocr_accuracy']}")

        Logger.separator()

        confirm = Logger.input_prompt("Start brute force? (y/n): ").strip().lower()
        return confirm == 'y'
