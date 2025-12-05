from PIL import Image
import io
import easyocr
import tempfile
import os

# Initialize reader once (load on first call)
_reader = None

def get_reader():
    """Lazy load OCR reader to avoid startup overhead"""
    global _reader
    if _reader is None:
        _reader = easyocr.Reader(['en'], gpu=False)
    return _reader

def read_captcha(img_bytes):
    """
    Extract text from CAPTCHA image bytes
    
    Args:
        img_bytes: PNG image bytes from screenshot
    
    Returns:
        Cleaned text string (uppercase alphanumeric only)
    """
    try:
        # Open image from bytes
        image = Image.open(io.BytesIO(img_bytes))
        
        # Scale up 5x for better OCR accuracy
        image = image.resize(
            (image.width * 5, image.height * 5), 
            Image.LANCZOS
        )
        
        # Save to temporary file (EasyOCR requires file path)
        with tempfile.NamedTemporaryFile(suffix='.png', delete=False) as tmp:
            tmp_path = tmp.name
            image.save(tmp_path)
        
        try:
            # Perform OCR
            reader = get_reader()
            results = reader.readtext(tmp_path)
            
            # Extract and concatenate text from all detected regions
            text = ''.join([result[1] for result in results])
            
            # Filter to CAPTCHA charset (uppercase alphanumeric)
            cleaned = ''.join(c for c in text.upper() 
                            if c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ23456789')
            
            return cleaned
        finally:
            # Clean up temporary file
            if os.path.exists(tmp_path):
                os.remove(tmp_path)
    
    except Exception as e:
        print(f"[!] OCR Error: {e}")
        return ""
