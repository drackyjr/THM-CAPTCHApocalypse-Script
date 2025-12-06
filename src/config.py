"""Configuration management"""

import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

class Config:
    """Base configuration class"""

    TARGET_URL = os.getenv("TARGET_URL", "http://10.48.184.96/index.php")
    TARGET_USERNAME = os.getenv("TARGET_USERNAME", "admin")
    WORDLIST_PATH = os.getenv("WORDLIST_PATH", "/usr/share/wordlists/rockyou.txt")
    MAX_PASSWORDS_TO_TRY = int(os.getenv("MAX_PASSWORDS_TO_TRY", "100"))
    MAX_WORKERS = int(os.getenv("MAX_WORKERS", "5"))
    WAIT_TIMEOUT = int(os.getenv("WAIT_TIMEOUT", "10"))
    PAGE_LOAD_WAIT = 1.5
    RESPONSE_WAIT = 2.5
    HEADLESS = True
    DISABLE_SANDBOX = True
    DISABLE_DEV_SHM = True
    OCR_ENGINE = os.getenv("OCR_ENGINE", "pytesseract")
    OCR_SCALE_FACTOR = 5
    USE_GPU = False
    TESSERACT_PATH = os.getenv("TESSERACT_PATH", "/usr/bin/tesseract")

    # CAPTCHA Strength Settings
    CAPTCHA_STRENGTH = os.getenv("CAPTCHA_STRENGTH", "medium")  # easy, medium, hard, extreme

current_config = Config()

# CAPTCHA Strength Descriptions
CAPTCHA_STRENGTHS = {
    "easy": {
        "description": "3 characters (letters + numbers)",
        "min_length": 3,
        "max_length": 3,
        "pattern": "Simple - Easy to OCR",
        "ocr_accuracy": "95%+"
    },
    "medium": {
        "description": "4-5 characters (letters + numbers)",
        "min_length": 4,
        "max_length": 5,
        "pattern": "Mix of letters & digits (like J4HUX)",
        "ocr_accuracy": "85-90%"
    },
    "hard": {
        "description": "5-6 characters (letters + numbers + symbols)",
        "min_length": 5,
        "max_length": 6,
        "pattern": "With special characters",
        "ocr_accuracy": "70-80%"
    },
    "extreme": {
        "description": "6-8 characters (distorted + rotated)",
        "min_length": 6,
        "max_length": 8,
        "pattern": "Distorted, rotated, blurred",
        "ocr_accuracy": "50-70%"
    }
}
