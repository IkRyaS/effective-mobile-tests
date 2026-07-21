from playwright.sync_api import Page

from src.pages.base_page import BasePage
from src.config import Config


class LoginPage(BasePage):

    URL = Config.URL_SAUCEDEMO_LOGIN

    def __init__(self, page: Page):
        super().__init__(page)

        self.input_login = page.locator("#user-name")
        self.input_password = page.locator("#password")
        self.login_button = page.locator("#login-button")

    def navigate_to_login_page(self):
        """Открывает страницу авторизации."""
        self.open(self.URL)

    def login(self, username: str, password: str):
        """Выполняет авторизацию пользователя.

        Args:
            username: Имя пользователя для авторизации.
            password: Пароль пользователя.

        Raises:
            PlaywrightError: Если поля не найдены или кнопка недоступна.
        """
        self.input_login.fill(username)
        self.input_password.fill(password)
        self.login_button.click()
