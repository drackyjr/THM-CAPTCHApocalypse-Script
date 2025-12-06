"""Utility logging functions"""

class Logger:
    """Color-coded console logger"""

    GREEN = '\033[92m'
    RED = '\033[91m'
    BLUE = '\033[94m'
    YELLOW = '\033[93m'
    CYAN = '\033[96m'
    MAGENTA = '\033[95m'
    RESET = '\033[00m'
    BOLD = '\033[1m'

    @staticmethod
    def success(message: str) -> None:
        print(f"{Logger.GREEN}{message}{Logger.RESET}")

    @staticmethod
    def error(message: str) -> None:
        print(f"{Logger.RED}{message}{Logger.RESET}")

    @staticmethod
    def info(message: str) -> None:
        print(f"{Logger.BLUE}{message}{Logger.RESET}")

    @staticmethod
    def warning(message: str) -> None:
        print(f"{Logger.YELLOW}{message}{Logger.RESET}")

    @staticmethod
    def input_prompt(message: str) -> str:
        """Print input prompt in cyan"""
        return input(f"{Logger.CYAN}{message}{Logger.RESET}")

    @staticmethod
    def separator(char: str = "=", length: int = 60) -> None:
        print(Logger.BLUE + (char * length) + Logger.RESET)

    @staticmethod
    def header(title: str) -> None:
        Logger.separator()
        print(f"{Logger.BOLD}{Logger.CYAN}{title.center(60)}{Logger.RESET}")
        Logger.separator()
