"""OCR Engine Factory"""

from typing import Optional
from .engines.pytesseract_engine import PytesseractOCREngine
from .engines.easyocr_engine import EasyOCREngine
from ..config import current_config
from ..utils import Logger

ENGINES = {
    'pytesseract': PytesseractOCREngine,
    'easyocr': EasyOCREngine,
}

class OCRFactory:
    """Factory to create OCR engine instances"""

    @staticmethod
    def create_ocr_processor(engine: Optional[str] = None, captcha_strength: str = "medium"):
        if engine is None:
            engine = current_config.OCR_ENGINE

        engine = engine.lower()

        if engine not in ENGINES:
            available = ', '.join(ENGINES.keys())
            raise ValueError(
                f"OCR engine '{engine}' not available. "
                f"Available: {available}"
            )

        Logger.info(f"[*] Using OCR Engine: {engine}")
        Logger.info(f"[*] CAPTCHA Strength: {captcha_strength}")

        if engine == 'pytesseract':
            return ENGINES['pytesseract'](
                scale_factor=current_config.OCR_SCALE_FACTOR,
                tesseract_path=current_config.TESSERACT_PATH,
                captcha_strength=captcha_strength
            )

        elif engine == 'easyocr':
            return ENGINES['easyocr'](
                scale_factor=current_config.OCR_SCALE_FACTOR,
                gpu=current_config.USE_GPU,
                captcha_strength=captcha_strength
            )
