from playwright.sync_api import Page

from src.ui.pages.base_page import BasePage
from src.config import SaucedemoConfig


class LoginPage(BasePage):
    """Страница авторизации пользователя."""

    URL = SaucedemoConfig.URL_SAUCEDEMO_LOGIN

    def __init__(self, page: Page) -> None:
        """Инициализирует страницу и локаторы элементов.

        Args:
            page: Объект страницы Playwright.
        """
        super().__init__(page)

        self.input_login = page.locator("#user-name")
        self.input_password = page.locator("#password")
        self.login_button = page.locator("#login-button")

    def navigate_to_login_page(self) -> None:
        """Открывает страницу авторизации."""
        self.open(self.URL)

    def login(self, username: str, password: str) -> None:
        """Выполняет авторизацию пользователя.

        Args:
            username: Имя пользователя для авторизации.
            password: Пароль пользователя.

        Raises:
            PlaywrightError: Если поля не найдены или кнопка недоступна.
            TimeoutError: Если элементы не стали доступны в течение таймаута.
        """
        self.input_login.fill(username)
        self.input_password.fill(password)
        self.login_button.click()