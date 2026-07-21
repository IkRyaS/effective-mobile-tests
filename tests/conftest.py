import pytest
from playwright.sync_api import sync_playwright

from src.config import Config


@pytest.fixture(scope="function")
def custom_page():
    """Создает и возвращает страницу Playwright для автоматизации браузера.

    Returns:
        Page: Объект страницы Playwright для взаимодействия с браузером.
    """
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=Config.HEADLESS)
        page = browser.new_page()
        yield page
        browser.close()