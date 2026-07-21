from playwright.sync_api import Page

from src.pages.base_page import BasePage


class InventoryPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)

        self.cart_link  = page.locator(".shopping_cart_link")
        self.product_item = page.locator(".inventory_item")

    def add_product_to_cart_by_name(self, product_name: str):
        """Добавляет товар в корзину по его названию.

        Args:
            product_name: Название товара для добавления.

        Raises:
            PlaywrightError: Если товар с указанным названием не найден.
        """
        target_product = self.product_item.filter(has_text=product_name)
        target_product.locator("button[id^='add-to-cart']").click()

    def click_cart_icon(self):
        """Переходит в корзину.

        Raises:
            PlaywrightError: Если иконка корзины не найдена.
        """
        self.cart_link.click()
