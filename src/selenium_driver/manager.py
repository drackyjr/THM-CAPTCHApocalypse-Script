"""Selenium WebDriver management"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class DriverManager:
    """Manages Selenium WebDriver lifecycle"""

    DEFAULT_USER_AGENT = (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    )

    def __init__(
        self,
        headless: bool = True,
        disable_sandbox: bool = True,
        disable_dev_shm: bool = True
    ):
        self.headless = headless
        self.disable_sandbox = disable_sandbox
        self.disable_dev_shm = disable_dev_shm

    def create_driver(self) -> webdriver.Chrome:
        options = Options()

        if self.headless:
            options.add_argument("--headless")

        if self.disable_sandbox:
            options.add_argument("--no-sandbox")

        if self.disable_dev_shm:
            options.add_argument("--disable-dev-shm-usage")

        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument(f"user-agent={self.DEFAULT_USER_AGENT}")
        options.add_argument("--disable-gpu")
        options.add_argument("--no-first-run")
        options.add_argument("--disable-sync")

        return webdriver.Chrome(options=options)

    @staticmethod
    def quit_driver(driver) -> None:
        if driver:
            try:
                driver.quit()
            except Exception as e:
                print(f"[!] Error quitting driver: {e}")
