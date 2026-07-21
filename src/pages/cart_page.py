from playwright.sync_api import Page

from src.pages.base_page import BasePage


class CartPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)

        self.cart_item_name = page.locator(".inventory_item_name")
        self.checkout_button = page.locator("#checkout")

    def get_product_names_in_cart(self) -> list[str]:
        """Возвращает список названий всех товаров в корзине.

        Returns:
            list[str]: Список названий товаров.
        """
        return self.cart_item_name.all_inner_texts()

    def click_checkout(self):
        """Нажимает кнопку перехода к оформлению заказа.

        Raises:
            PlaywrightError: Если кнопка не найдена или неактивна.
        """
        self.checkout_button.click()