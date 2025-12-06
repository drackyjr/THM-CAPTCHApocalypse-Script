# THM-CAPTCHApocalypse-Script

# Features Overview - v3.2

## 🆕 CAPTCHA Strength Selection

Select from 4 difficulty levels:

### EASY (1) - 3 Characters
- Plain letters + numbers
- Examples: ABC123, XYZ789
- OCR Accuracy: 95%+
- Image Scaling: 3x
- Best For: Testing, basic logins

### MEDIUM (2) - 4-5 Characters ⭐ Your Type
- Mix of letters and numbers
- Examples: J4HUX, P2KL9, M3QRS
- OCR Accuracy: 85-90%
- Image Scaling: 5x
- Best For: Standard CAPTCHAs
- Auto-enhancements: Contrast boost

### HARD (3) - 5-6 Characters
- With special characters
- Examples: 4J@2K9, P#L8M3
- OCR Accuracy: 70-80%
- Image Scaling: 7x
- Best For: Secured CAPTCHAs
- Auto-enhancements: Auto-contrast + edge detection

### EXTREME (4) - 6-8 Characters
- Heavily distorted/rotated
- Examples: Distorted patterns
- OCR Accuracy: 50-70%
- Image Scaling: 10x
- Best For: Maximum security
- Auto-enhancements: Full preprocessing

## 🔧 Automatic Adjustments

The tool automatically adjusts based on selected strength:

```
EASY      → scale_factor=3,  threshold=150
MEDIUM    → scale_factor=5,  threshold=130
HARD      → scale_factor=7,  threshold=110
EXTREME   → scale_factor=10, threshold=100
```

## 📊 Statistics Tracking

- Total attempts
- Failed CAPTCHA reads
- Success/failure ratio
- Elapsed time
- Attempts per second

## 🎯 OCR Recommendations

| Strength | Pytesseract | EasyOCR |
|----------|-------------|---------|
| Easy | ✅ Excellent | ✅ Excellent |
| Medium | ✅ Very Good | ✅ Excellent |
| Hard | ⚠️ Good | ✅ Very Good |
| Extreme | ❌ Poor | ✅ Good |

---

**Choose the right strength for maximum success!**
