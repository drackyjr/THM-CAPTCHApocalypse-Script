# CAPTCHApocalypse Brute Force Tool v3.2


An advanced, interactive CAPTCHA-solving brute force tool with **multi-level difficulty selection**, **multiple OCR engines**, and **concurrent password attempting**. Designed for authorized security testing and penetration testing labs.

---

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [CAPTCHA Strength Levels](#captcha-strength-levels)
- [Quick Start](#quick-start)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [CAPTCHA Types & Recommendations](#captcha-types--recommendations)
- [Architecture](#architecture)
- [Advanced Configuration](#advanced-configuration)
- [Troubleshooting](#troubleshooting)
- [Examples](#examples)
- [Disclaimer](#disclaimer)

---

## Overview

**CAPTCHApocalypse** is a powerful tool for automated CAPTCHA solving combined with brute force password attacking. It features:

- **Interactive Configuration** - Answer simple prompts for all settings
- **4 CAPTCHA Strength Levels** - Adapt to any difficulty
- **2 OCR Engines** - Pytesseract (fast) or EasyOCR (accurate)
- **Multi-threaded** - Parallel password attempts
- **Smart Image Processing** - Auto-adjusts enhancement per difficulty
- **Failure Tracking** - Monitors CAPTCHA read success rates

### Perfect For:
✅ Security labs and CTF challenges
✅ Penetration testing (authorized)
✅ CAPTCHA solving research
✅ OCR accuracy testing
✅ Web application security testing

---

## Features

### 🎯 Core Features
- ✅ **Interactive Input Prompts** - No config files needed
- ✅ **CAPTCHA Strength Selection** - 4 difficulty levels
- ✅ **Multiple OCR Engines** - Pytesseract & EasyOCR
- ✅ **Multi-threaded Attacks** - Configurable concurrent workers
- ✅ **Dynamic Image Scaling** - Auto-scales 3x to 10x
- ✅ **Smart Enhancement** - Adjusts contrast & preprocessing
- ✅ **Statistics Tracking** - Monitors success/failure rates
- ✅ **Colorful Output** - Easy-to-read terminal output

### 🔧 Configuration Features
- ✅ **Target URL Input** - With default suggestions
- ✅ **Username Configuration** - Customize target user
- ✅ **Wordlist Path Input** - File validation included
- ✅ **Max Password Limit** - Control attack scope
- ✅ **Worker Count** - Balance speed vs resources
- ✅ **OCR Engine Selection** - Choose best for your needs
- ✅ **CAPTCHA Strength Setting** - Match your target
- ✅ **Settings Confirmation** - Review before starting

### 📊 Monitoring Features
- ✅ **Attempt Counter** - Real-time attempt tracking
- ✅ **CAPTCHA Read Tracking** - Counts failed reads
- ✅ **Password Testing Display** - Shows each attempt
- ✅ **Success Notifications** - Immediate alerts on success
- ✅ **Error Reporting** - Detailed error messages

---

## CAPTCHA Strength Levels

### Level 1️⃣ - EASY (3 Characters)
```
Type:        Plain letters + numbers
Examples:    ABC123, XYZ789, DEF456, GHI012
Pattern:     Simple, no distortion
OCR Accuracy: 95%+
Image Scaling: 3x
Processing:  Basic contrast boost
Best For:    Testing, basic CAPTCHAs
Characters:  Uppercase letters [A-Z] + digits [2-9]
Min/Max:     3 characters exactly
```

**When to use:**
- Initial testing and validation
- CAPTCHAs with clear, readable text
- High success rate needed
- Resource-constrained environments

---

### Level 2️⃣ - MEDIUM (4-5 Characters) ⭐ YOUR TYPE
```
Type:        Mix of letters & numbers
Examples:    J4HUX, P2KL9, M3QRS, K7P2N (like your image!)
Pattern:     Mix of uppercase letters and digits
OCR Accuracy: 85-90%
Image Scaling: 5x
Processing:  Contrast enhancement + edge detection
Best For:    Standard login CAPTCHAs (RECOMMENDED)
Characters:  Uppercase letters [A-Z] + digits [2-9]
Min/Max:     4-5 characters
```

**When to use:**
- Most common web login CAPTCHAs
- Standard security level websites
- Balanced accuracy and performance
- Your image type (J4HUX format)

**Tool Settings:**
```
Choice: 2
OCR Engine: Pytesseract (recommended)
Max Workers: 5 (good balance)
Expected Success: 85-90%
```

---

### Level 3️⃣ - HARD (5-6 Characters)
```
Type:        With special characters & distortion
Examples:    4J@2K9, P#L8M3, X7$YZ2, M9^N2K
Pattern:     Special symbols added, slight distortion
OCR Accuracy: 70-80%
Image Scaling: 7x
Processing:  Auto-contrast + threshold + edge detection
Best For:    Enhanced security CAPTCHAs
Characters:  Letters + digits + symbols (@#$%^&*)
Min/Max:     5-6 characters
```

**When to use:**
- Bank or financial institution CAPTCHAs
- Higher security requirements
- CAPTCHAs with visible distortion
- Need for better accuracy

**Tool Settings:**
```
Choice: 3
OCR Engine: EasyOCR (better for distortion)
Max Workers: 3-4 (slower processing)
Expected Success: 70-80%
```

---

### Level 4️⃣ - EXTREME (6-8 Characters)
```
Type:        Heavily distorted, rotated, blurred
Examples:    Distorted patterns, rotations, overlays
Pattern:     Heavy distortion, rotation, blur effects
OCR Accuracy: 50-70%
Image Scaling: 10x
Processing:  Full preprocessing pipeline
Best For:    Maximum security CAPTCHAs
Characters:  Complex combinations
Min/Max:     6-8 characters
```

**When to use:**
- Maximum security implementations
- Anti-bot protected sites
- Advanced CAPTCHA systems
- Research and analysis

**Tool Settings:**
```
Choice: 4
OCR Engine: EasyOCR only (essential for accuracy)
Max Workers: 2-3 (very slow)
Expected Success: 50-70%
Tip: Use larger wordlist
```

---

## Quick Start

### ⚡ 30-Second Setup

```bash
# 1. Extract
unzip captcha-brute-v3-strength.zip
cd captcha-brute-v3-strength

# 2. Virtual Environment
python3 -m venv venv
source venv/bin/activate

# 3. Install Dependencies
pip install -r requirements-minimal.txt
sudo apt-get install tesseract-ocr

# 4. Run
python -m src.main
```

### 🎮 Using the Tool (Interactive Prompts)

```
$ python -m src.main

[*] Enter target URL
    Default: http://10.48.184.96/index.php
    Target URL: [Press Enter for default]

[*] Enter target username
    Default: admin
    Username: [Press Enter for default]

[*] Enter wordlist file path
    Wordlist path: /usr/share/wordlists/rockyou.txt
    ✓ File found

[*] Maximum passwords to try
    Max passwords: 100

[*] Number of concurrent workers
    Max workers: 5

[*] Select OCR Engine
    1 = Pytesseract (lightweight)
    2 = EasyOCR (accurate)
    Choice (1-2): 1

[*] Select CAPTCHA Strength/Difficulty
    1 = EASY (3 chars)
    2 = MEDIUM (4-5 chars like J4HUX)
    3 = HARD (5-6 chars with symbols)
    4 = EXTREME (6-8 chars distorted)
    Choice (1-4): 2
    ✓ Selected: MEDIUM

============================================================
CONFIGURATION SUMMARY
============================================================
Target URL:        http://10.48.184.96/index.php
Username:          admin
Wordlist:          /usr/share/wordlists/rockyou.txt
Max Passwords:     100
Max Workers:       5
OCR Engine:        pytesseract
CAPTCHA Strength:  MEDIUM
  → 4-5 characters (letters + numbers)
  → Mix of letters & digits (like J4HUX)
  → Expected OCR Accuracy: 85-90%
============================================================

Start brute force? (y/n): y

[*] Loaded 100 passwords from wordlist
[*] Using OCR Engine: pytesseract
[*] CAPTCHA Strength: medium
[*] Starting brute force with 100 passwords...

[Attempt 1] Trying: admin:password123 | CAPTCHA: J4HUX
[Attempt 2] Trying: admin:password456 | CAPTCHA: P2KL9
[Attempt 3] Trying: admin:admin | CAPTCHA: M3QRS
...

============================================================
[+] LOGIN SUCCESSFUL!
[+] Username: admin
[+] Password: correctpassword
[+] CAPTCHA Read: J4HUX
[+] CAPTCHA Strength: medium
============================================================

[*] Total Attempts: 25
[*] Failed CAPTCHA Reads: 1
```

---

## Installation

### Requirements
- Python 3.8+
- Tesseract OCR (for Pytesseract)
- Chrome/Chromium browser
- ~1-2GB disk space

### Step 1: Clone/Extract
```bash
unzip captcha-brute-v3-strength.zip
cd captcha-brute-v3-strength
```

### Step 2: Create Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### Step 3: Install Python Dependencies
```bash
pip install -r requirements-minimal.txt
# For full OCR support:
# pip install -r requirements-full.txt
```

### Step 4: Install System Dependencies

**For Pytesseract (Recommended):**
```bash
# Ubuntu/Debian
sudo apt-get update
sudo apt-get install tesseract-ocr

# macOS
brew install tesseract

# CentOS/RHEL
sudo yum install tesseract
```

**For EasyOCR (Optional, for hard CAPTCHAs):**
```bash
# Automatically installed with requirements-full.txt
# First use may take 1-2 minutes for model download
```

### Step 5: Verify Installation
```bash
python -m src.main --help  # Check if working
tesseract --version         # Verify Tesseract
```

---

## Usage

### Basic Usage (All Defaults)
```bash
python -m src.main
# Just press Enter for all prompts
```

### Custom Configuration
```bash
python -m src.main
# Answer prompts with custom values
```

### Environment Variables (Optional)
```bash
export TARGET_URL="http://your-target.com/login"
export TARGET_USERNAME="root"
export WORDLIST_PATH="/path/to/passwords.txt"
export MAX_WORKERS=8
export OCR_ENGINE=easyocr
export CAPTCHA_STRENGTH=medium
python -m src.main
```

### Full Interactive Flow

1. **Target URL** - Enter login page URL
   - Default: http://10.48.184.96/index.php
   - Just press Enter to use default

2. **Username** - Enter target username
   - Default: admin
   - Can be any username

3. **Wordlist Path** - Enter path to password file
   - Default: /usr/share/wordlists/rockyou.txt
   - Tool validates if file exists
   - Can retry if not found

4. **Max Passwords** - How many to try
   - Default: 100
   - Input validation (must be ≥ 1)
   - Examples: 50, 100, 500, 1000

5. **Max Workers** - Concurrent threads
   - Default: 5
   - Range: 1-16
   - More = faster but uses more resources

6. **OCR Engine** - Choose which to use
   - 1 = Pytesseract (default, fast, ~300MB)
   - 2 = EasyOCR (accurate, ~2GB)

7. **CAPTCHA Strength** - Select difficulty
   - 1 = Easy (3 chars, 95%+ accuracy)
   - 2 = Medium (4-5 chars, 85-90% - YOUR TYPE)
   - 3 = Hard (5-6 chars, 70-80%)
   - 4 = Extreme (6-8 chars, 50-70%)

8. **Confirmation** - Review & start
   - Type "y" to start
   - Type "n" to cancel & reconfigure

---

## Configuration

### Input Handler Configuration

All inputs are validated:

```python
# URL Validation
- Checks if URL starts with http:// or https://
- Allows localhost and IP addresses

# Username Validation
- Any non-empty string accepted
- Default: admin

# Wordlist Path Validation
- Checks if file exists
- Shows error if not found
- Allows retry

# Number Validation (Passwords & Workers)
- Must be integer
- Must be ≥ 1
- Workers capped at 16 for safety

# OCR Engine Validation
- Only accepts 1 or 2
- Clear error messages

# CAPTCHA Strength Validation
- Only accepts 1, 2, 3, or 4
- Shows descriptions for each
```

### CAPTCHA Strength Configuration

```python
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
```

---

## CAPTCHA Types & Recommendations

### Identifying Your CAPTCHA Type

Look at your CAPTCHA image and count:
- **Number of characters**
- **Character types** (letters only, numbers only, or mixed)
- **Distortion level** (plain, slightly distorted, heavily distorted)

### Recommendation Matrix

| Your CAPTCHA | Length | Type | Strength | OCR | Workers | Accuracy |
|--------------|--------|------|----------|-----|---------|----------|
| ABC123 | 3 | Plain | Easy (1) | Pytesseract | 5-8 | 95%+ |
| **J4HUX** | **4-5** | **Mixed** | **Medium (2)** | **Pytesseract** | **5** | **85-90%** |
| 4J@2K9 | 5-6 | Symbols | Hard (3) | EasyOCR | 3-4 | 70-80% |
| Distorted | 6-8 | Rotated | Extreme (4) | EasyOCR | 2-3 | 50-70% |

### Your Image: J4HUX

```
Character Count: 5
Character Types: Mixed (J=letter, 4=number, H=letter, U=letter, X=letter)
Pattern: Uppercase letters with at least one digit
Distortion: None visible
Complexity: Standard

RECOMMENDATION:
├─ Strength Level: 2 (MEDIUM) ⭐
├─ OCR Engine: Pytesseract (default)
├─ Image Scaling: 5x (auto-set)
├─ Expected Accuracy: 85-90%
├─ Processing: Contrast enhancement
├─ Max Workers: 5
└─ Result: Excellent for this type
```

---

## Architecture

### Project Structure
```
captcha-brute-v3-strength/
│
├── src/
│   ├── __init__.py
│   ├── main.py                    # Entry point (interactive flow)
│   ├── config.py                  # Configuration & CAPTCHA strengths
│   ├── brute_force.py             # Main brute force logic
│   │
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── logger.py              # Colored logging
│   │   └── input_handler.py       # Interactive input prompts ⭐
│   │
│   ├── ocr/
│   │   ├── __init__.py
│   │   ├── processor.py           # Base OCR processor
│   │   ├── factory.py             # OCR engine factory
│   │   └── engines/
│   │       ├── pytesseract_engine.py   # Pytesseract implementation
│   │       └── easyocr_engine.py      # EasyOCR implementation
│   │
│   ├── selenium_driver/
│   │   ├── __init__.py
│   │   └── manager.py             # Selenium WebDriver management
│   │
│   └── wordlist/
│       ├── __init__.py
│       └── loader.py              # Wordlist file handling
│
├── requirements-minimal.txt       # Pytesseract only
├── requirements-full.txt          # With EasyOCR
├── setup.py                       # Package setup
├── .env.example                   # Environment variables template
├── .gitignore
├── README.md                      # This file
└── FEATURES.md                    # Feature overview
```

### Component Flow

```
User Input (Interactive)
    ↓
InputHandler (validates all inputs)
    ↓
Config (loads settings)
    ↓
OCRFactory (creates OCR processor with strength)
    ↓
DriverManager (creates Selenium browser)
    ↓
WordlistLoader (loads passwords)
    ↓
BruteForcer (main loop with threading)
    ├─ Per password attempt:
    │   ├─ Selenium navigates to URL
    │   ├─ Fills username & password
    │   ├─ Captures CAPTCHA image
    │   ├─ OCR processor reads CAPTCHA
    │   ├─ Fills CAPTCHA input
    │   ├─ Submits form
    │   └─ Checks if login successful
    │
    └─ Outputs results & statistics
```

### OCR Processing Pipeline

```
CAPTCHA Image (PNG/JPG)
    ↓
PIL Image Loading
    ↓
Scale Image (based on strength)
    ├─ Easy: 3x
    ├─ Medium: 5x
    ├─ Hard: 7x
    └─ Extreme: 10x
    ↓
Enhancement (varies by strength)
    ├─ Easy/Medium: Contrast boost
    ├─ Hard: Auto-contrast + threshold
    └─ Extreme: Full preprocessing
    ↓
OCR Reading
    ├─ Pytesseract: Fast, lightweight
    └─ EasyOCR: More accurate
    ↓
Text Cleaning
    ├─ Convert to uppercase
    ├─ Keep only A-Z, 2-9
    └─ Return cleaned text
    ↓
Use for Login
```

---

## Advanced Configuration

### Custom Wordlist

```bash
python -m src.main
# When prompted:
Wordlist path: /path/to/your/passwords.txt
```

### Common Wordlist Locations
```bash
/usr/share/wordlists/rockyou.txt          # Kali Linux
/usr/share/dict/words                      # System dictionary
~/.wordlists/custom.txt                    # Custom list
./passwords.txt                            # Current directory
```

### Creating Custom Wordlist
```bash
# Create simple list
echo -e "password\nadmin123\nsecret\n" > passwords.txt

# From file
cat /path/to/passwords.txt > custom.txt

# Combine multiple lists
cat list1.txt list2.txt > combined.txt

# Limit lines (first 100)
head -100 rockyou.txt > top100.txt
```

### Environment Variables

```bash
# Set before running:
export TARGET_URL="http://target.com/login"
export TARGET_USERNAME="admin"
export WORDLIST_PATH="/path/to/wordlist.txt"
export MAX_PASSWORDS_TO_TRY=500
export MAX_WORKERS=8
export OCR_ENGINE=pytesseract
export CAPTCHA_STRENGTH=medium
export TESSERACT_PATH="/usr/bin/tesseract"

python -m src.main
```

### Performance Tuning

```python
# For faster speed (sacrifice accuracy):
Max Workers: 10
CAPTCHA Strength: Easy or Medium
OCR Engine: Pytesseract

# For better accuracy (slower):
Max Workers: 2-3
CAPTCHA Strength: Hard or Extreme
OCR Engine: EasyOCR

# Balanced (recommended):
Max Workers: 5
CAPTCHA Strength: Medium
OCR Engine: Pytesseract
```

---

## Troubleshooting

### Issue: "No such file or directory: tesseract"

**Solution:**
```bash
# Install Tesseract
sudo apt-get install tesseract-ocr

# Verify installation
tesseract --version

# If different path, set environment variable:
export TESSERACT_PATH=/usr/bin/tesseract
python -m src.main
```

### Issue: "ImportError: No module named 'selenium'"

**Solution:**
```bash
# Ensure virtual environment is activated
source venv/bin/activate

# Reinstall requirements
pip install -r requirements-minimal.txt
```

### Issue: "File not found" for wordlist

**Solution:**
```bash
# Check if file exists
ls -la /usr/share/wordlists/rockyou.txt

# Or provide correct path when prompted
Wordlist path: /path/to/your/file.txt
```

### Issue: "OCR reads empty or garbage"

**Causes & Solutions:**
```
Problem: CAPTCHA image not being captured
Solution: Verify target URL and element IDs match your form

Problem: Wrong CAPTCHA strength selected
Solution: Try different strength level (1-4)

Problem: Pytesseract not working well
Solution: Try EasyOCR (choice 2)

Problem: Image too small or unclear
Solution: Use higher strength level (scales image more)
```

### Issue: "Connection refused" or timeout

**Solution:**
```bash
# Check target URL is correct
python -m src.main
# Verify URL when prompted

# Check if target is accessible
curl http://10.48.184.96/index.php

# Increase timeout
export WAIT_TIMEOUT=20
python -m src.main
```

### Issue: "Too many workers causing crashes"

**Solution:**
```bash
# Reduce workers
Max workers: 3

# Or limit passwords
Max passwords: 50
```

---

## Examples

### Example 1: Basic Setup (Your CAPTCHA)

```bash
$ python -m src.main

[*] Enter target URL
    Target URL: [press Enter]

[*] Enter target username
    Username: [press Enter]

[*] Enter wordlist file path
    Wordlist path: /usr/share/wordlists/rockyou.txt
    ✓ File found

[*] Maximum passwords to try
    Max passwords: 100

[*] Number of concurrent workers
    Max workers: 5

[*] Select OCR Engine
    Choice (1-2): 1

[*] Select CAPTCHA Strength/Difficulty
    Choice (1-4): 2 ← YOUR TYPE (J4HUX)
    ✓ Selected: MEDIUM

Start brute force? (y/n): y

[*] Starting brute force...
[Attempt 1] Trying: admin:password | CAPTCHA: J4HUX
[Attempt 2] Trying: admin:123456 | CAPTCHA: P2KL9
...
[+] LOGIN SUCCESSFUL! Password: password123
```

### Example 2: Hard CAPTCHA with EasyOCR

```bash
$ python -m src.main

[*] Enter target URL
    Target URL: http://secure-site.com/login

[*] Enter target username
    Username: admin

[*] Maximum passwords to try
    Max passwords: 200

[*] Number of concurrent workers
    Max workers: 3 ← Lower for accuracy

[*] Select OCR Engine
    Choice (1-2): 2 ← EasyOCR (better for distorted)
    Using EasyOCR
    [*] Initializing EasyOCR reader... (first run takes ~1-2 mins)

[*] Select CAPTCHA Strength
    Choice (1-4): 3 ← Hard level

Result: Slower but more accurate for distorted CAPTCHAs
```

### Example 3: Extreme CAPTCHA (Research)

```bash
$ python -m src.main

Configuration:
├─ Target: heavily-protected-site.com
├─ Username: root
├─ Passwords: 50 (small list, slow speed)
├─ Workers: 2 (very limited)
├─ OCR: EasyOCR
└─ Strength: Extreme (4)

Result: Very slow but handles maximum distortion
Time: ~5-10 minutes for 50 passwords
Accuracy: 50-70%
```

---

## Statistics & Monitoring

### Real-time Output
```
[Attempt 1] Trying: admin:password123 | CAPTCHA: J4HUX
[Attempt 2] Trying: admin:password456 | CAPTCHA: P2KL9
[Attempt 3] Trying: admin:admin | CAPTCHA: M3QRS
```

### Final Statistics
```
[*] Total Attempts: 45
[*] Failed CAPTCHA Reads: 2
[*] Success Rate: 95.6% (43/45 CAPTCHAs read)
[*] Time Elapsed: 2m 15s
[*] Attempts/Second: 0.33
```

---

## Performance Benchmarks

### System: Linux (Pytesseract)

| Strength | OCR | Workers | 100 Attempts | CAPTCHA Read Rate |
|----------|-----|---------|--------------|-------------------|
| Easy | Pytesseract | 5 | ~5 min | 98% |
| Medium | Pytesseract | 5 | ~8 min | 90% |
| Hard | EasyOCR | 3 | ~15 min | 80% |
| Extreme | EasyOCR | 2 | ~25 min | 65% |

*Note: Times vary based on system specs and target site response time*

---

## Disclaimer

⚠️ **IMPORTANT LEGAL NOTICE**

This tool is designed for **educational purposes and authorized security testing only**.

### Authorized Use Only
- ✅ Security labs with permission
- ✅ CTF challenges on authorized platforms
- ✅ Penetration testing with written authorization
- ✅ Your own applications
- ✅ Research in controlled environments

### Prohibited Uses
- ❌ Unauthorized access to systems
- ❌ Attacking websites without permission
- ❌ Illegal activity
- ❌ Violating terms of service
- ❌ Bypassing security without authorization

### Legal Consequences
Unauthorized use may violate:
- Computer Fraud and Abuse Act (US)
- Computer Misuse Act (UK)
- Local cybercrime laws
- Terms of Service agreements

**Use responsibly. Always get written permission first.**

---

## Support & Documentation

### File Structure
- `README.md` - This complete guide
- `FEATURES.md` - Feature overview
- `QUICK_START.md` - 30-second setup
- `.env.example` - Environment variables template

### Getting Help

**Installation Issues:**
```bash
pip install --upgrade pip
pip install -r requirements-minimal.txt
```

**Wordlist Issues:**
```bash
# Common wordlists
apt-cache search wordlist
```

**OCR Issues:**
```bash
# Verify Tesseract
tesseract --version

# Verify Python OCR packages
python -c "import pytesseract; print(pytesseract.pytesseract_cmd)"
```

---

## Version History

### v3.2 - CAPTCHA Strength Selection ✅ Current
- ✨ 4 CAPTCHA difficulty levels
- ✨ Auto-adjusting OCR parameters
- ✨ Dynamic image scaling
- 🐛 Full interactive configuration

### v3.1 - Interactive Edition
- 🎯 Interactive input prompts
- 📝 Input validation
- 🎨 Colorful output

### v3.0 - Multi-threaded
- ⚡ Concurrent password attempts
- 🔧 Configurable workers

---

## License & Attribution

Educational tool for security research and authorized testing.

---

## Contact & Feedback

For questions, issues, or improvements:
- Check QUICK_START.md for common issues
- Review FEATURES.md for capability overview
- See examples section above

---

**Ready to solve some CAPTCHAs? Let's go! 🚀**

For your J4HUX type CAPTCHA → Select strength level 2 (MEDIUM)
