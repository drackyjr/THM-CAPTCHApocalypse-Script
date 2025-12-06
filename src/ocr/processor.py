"""Base OCR processing module"""

from abc import ABC, abstractmethod

class BaseOCRProcessor(ABC):
    """Abstract base class for OCR processors"""

    CAPTCHA_CHARSET = set('ABCDEFGHIJKLMNOPQRSTUVWXYZ23456789')

    def __init__(self, scale_factor: int = 5, captcha_strength: str = "medium"):
        self.scale_factor = scale_factor
        self.captcha_strength = captcha_strength
        self.set_ocr_params()

    def set_ocr_params(self):
        """Set OCR parameters based on CAPTCHA strength"""
        strength_params = {
            "easy": {"scale_factor": 3, "threshold": 150},
            "medium": {"scale_factor": 5, "threshold": 130},
            "hard": {"scale_factor": 7, "threshold": 110},
            "extreme": {"scale_factor": 10, "threshold": 100}
        }

        if self.captcha_strength in strength_params:
            params = strength_params[self.captcha_strength]
            self.scale_factor = params["scale_factor"]
            self.threshold = params["threshold"]

    @abstractmethod
    def read_captcha(self, img_bytes: bytes) -> str:
        pass

    @staticmethod
    def clean_text(text: str) -> str:
        return ''.join(
            c for c in text.upper() 
            if c in BaseOCRProcessor.CAPTCHA_CHARSET
        )
