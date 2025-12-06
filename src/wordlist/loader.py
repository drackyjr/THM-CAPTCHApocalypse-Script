"""Wordlist loading and management"""

from typing import List

class WordlistLoader:
    """Handles wordlist file operations"""

    @staticmethod
    def load_passwords(wordlist_path: str, limit: int = 100) -> List[str]:
        passwords = []

        try:
            with open(wordlist_path, "r", encoding='utf-8', errors='ignore') as f:
                for i, line in enumerate(f):
                    if i >= limit:
                        break

                    pwd = line.strip()
                    if pwd:
                        passwords.append(pwd)

            print(f"[*] Loaded {len(passwords)} passwords from wordlist")
            return passwords

        except FileNotFoundError:
            print(f"[!] Wordlist not found: {wordlist_path}")
            raise

        except Exception as e:
            print(f"[!] Error loading wordlist: {e}")
            raise
