"""EasyOCR Engine"""

from PIL import Image
import io
import tempfile
import os

try:
    import easyocr
except ImportError:
    easyocr = None

from ..processor import BaseOCRProcessor

class EasyOCREngine(BaseOCRProcessor):
    """EasyOCR processor"""

    _reader = None

    def __init__(self, scale_factor: int = 5, gpu: bool = False, captcha_strength: str = "medium"):
        super().__init__(scale_factor, captcha_strength)

        if easyocr is None:
            raise ImportError(
                "easyocr not installed. Install with: pip install easyocr"
            )

        self.gpu = gpu

    @classmethod
    def get_reader(cls, gpu: bool = False):
        if cls._reader is None:
            print("[*] Initializing EasyOCR reader (first run takes ~1-2 minutes)...")
            cls._reader = easyocr.Reader(['en'], gpu=gpu)
        return cls._reader

    def read_captcha(self, img_bytes: bytes) -> str:
        try:
            image = Image.open(io.BytesIO(img_bytes))

            new_size = (
                image.width * self.scale_factor,
                image.height * self.scale_factor
            )
            image = image.resize(new_size, Image.LANCZOS)

            with tempfile.NamedTemporaryFile(suffix='.png', delete=False) as tmp:
                tmp_path = tmp.name
                image.save(tmp_path)

            try:
                reader = self.get_reader(gpu=self.gpu)
                results = reader.readtext(tmp_path)
                text = ''.join([result[1] for result in results])
                return self.clean_text(text)

            finally:
                if os.path.exists(tmp_path):
                    os.remove(tmp_path)

        except Exception as e:
            print(f"[!] EasyOCR Error: {e}")
            return ""
