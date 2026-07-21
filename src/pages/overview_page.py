from playwright.sync_api import Page

from src.pages.base_page import BasePage


class OverviewPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)

        self.finish_button = page.locator("#finish")

    def click_finish(self):
        """Нажимает кнопку завершения оформления заказа.

        Raises:
            PlaywrightError: Если кнопка не найдена или недоступна для клика.
        """
        self.finish_button.click()