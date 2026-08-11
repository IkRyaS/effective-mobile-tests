from playwright.sync_api import Page

from src.ui.pages.base_page import BasePage


class CartPage(BasePage):
    """Страница корзины с товарами."""

    def __init__(self, page: Page) -> None:
        """Инициализирует страницу и локаторы элементов.

        Args:
            page: Объект страницы Playwright.
        """
        super().__init__(page)

        self.cart_item_name = page.locator(".inventory_item_name")
        self.checkout_button = page.locator("#checkout")

    def get_product_names_in_cart(self) -> list[str]:
        """Возвращает список названий всех товаров в корзине.

        Returns:
            list[str]: Список названий товаров.
        """
        return self.cart_item_name.all_inner_texts()

    def click_checkout(self) -> None:
        """Нажимает кнопку перехода к оформлению заказа.

        Raises:
            PlaywrightError: Если кнопка не найдена или неактивна.
            TimeoutError: Если кнопка не стала доступна в течение таймаута.
        """
        self.checkout_button.click()