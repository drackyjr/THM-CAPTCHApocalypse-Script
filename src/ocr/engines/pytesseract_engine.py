"""Pytesseract OCR Engine"""

from PIL import Image
import io
from typing import Optional

try:
    import pytesseract
except ImportError:
    pytesseract = None

from ..processor import BaseOCRProcessor

class PytesseractOCREngine(BaseOCRProcessor):
    """Pytesseract OCR processor"""

    def __init__(self, scale_factor: int = 5, tesseract_path: Optional[str] = None, captcha_strength: str = "medium"):
        super().__init__(scale_factor, captcha_strength)

        if pytesseract is None:
            raise ImportError(
                "pytesseract not installed. Install with: "
                "pip install pytesseract && apt-get install tesseract-ocr"
            )

        if tesseract_path:
            pytesseract.pytesseract.pytesseract_cmd = tesseract_path

    def read_captcha(self, img_bytes: bytes) -> str:
        try:
            image = Image.open(io.BytesIO(img_bytes))

            # Scale based on CAPTCHA strength
            new_size = (
                image.width * self.scale_factor,
                image.height * self.scale_factor
            )
            image = image.resize(new_size, Image.LANCZOS)

            # Enhance based on strength
            from PIL import ImageEnhance, ImageOps

            # For harder CAPTCHAs, apply more enhancement
            if self.captcha_strength in ["hard", "extreme"]:
                # Apply threshold to reduce noise
                image = ImageOps.autocontrast(image)

            enhancer = ImageEnhance.Contrast(image)
            image = enhancer.enhance(2)

            text = pytesseract.image_to_string(image, config='--psm 6')
            return self.clean_text(text)

        except Exception as e:
            print(f"[!] Pytesseract OCR Error: {e}")
            return ""
