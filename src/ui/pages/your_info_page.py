from playwright.sync_api import Page

from src.ui.pages.base_page import BasePage


class YourInfoPage(BasePage):
    """Страница ввода персональной информации покупателя."""

    def __init__(self, page: Page) -> None:
        """Инициализирует страницу и локаторы элементов.

        Args:
            page: Объект страницы Playwright.
        """
        super().__init__(page)

        self.first_name = page.locator("#first-name")
        self.last_name = page.locator("#last-name")
        self.mail_index = page.locator("#postal-code")
        self.continue_button = page.locator("#continue")

    def fill_out_data(self, first_name: str, last_name: str, mail_index: str) -> None:
        """Заполняет персональные данные покупателя и переходит к подтверждению.

        Args:
            first_name: Имя покупателя.
            last_name: Фамилия покупателя.
            mail_index: Почтовый индекс.

        Raises:
            PlaywrightError: Если поля не найдены или кнопка недоступна.
            TimeoutError: Если элементы не стали доступны в течение таймаута.
        """
        self.first_name.fill(first_name)
        self.last_name.fill(last_name)
        self.mail_index.fill(mail_index)
        self.continue_button.click()