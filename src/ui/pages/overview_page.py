from playwright.sync_api import Page

from src.ui.pages.base_page import BasePage


class OverviewPage(BasePage):
    """Страница обзора заказа перед подтверждением."""

    def __init__(self, page: Page) -> None:
        """Инициализирует страницу и локаторы элементов.

        Args:
            page: Объект страницы Playwright.
        """
        super().__init__(page)

        self.finish_button = page.locator("#finish")

    def click_finish(self) -> None:
        """Нажимает кнопку завершения оформления заказа.

        Raises:
            PlaywrightError: Если кнопка не найдена или недоступна для клика.
            TimeoutError: Если кнопка не стала доступна в течение таймаута.
        """
        self.finish_button.click()