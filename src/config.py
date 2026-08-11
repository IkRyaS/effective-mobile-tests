import os
from dotenv import load_dotenv

load_dotenv()


class SaucedemoConfig:
    """Конфигурация для тестирования веб-ресурса Saucedemo.com"""
    URL_SAUCEDEMO_LOGIN = os.getenv('SAUCEDEMO_LOGIN', "https://www.saucedemo.com/")
    URL_SAUCEDEMO_INVENTORY = os.getenv('SAUCEDEMO_INVENTORY', "https://www.saucedemo.com/inventory.html")
    URL_SAUCEDEMO_CHECKOUT_COMPLETE = os.getenv('SAUCEDEMO_CHECKOUT_COMPLETE', "https://www.saucedemo.com/checkout-complete.html")
    HEADLESS = os.getenv('HEADLESS', 'false').lower() == 'true'


class GitHubConfig:
    """Конфигурация для интеграции с GitHub REST API."""
    URL_GITHUB = os.getenv('GITHUB', "https://api.github.com")
    GITHUB_API_TOKEN = os.getenv('GITHUB_API_TOKEN', '')
    GITHUB_USERNAME = os.getenv('GITHUB_USERNAME', '')
