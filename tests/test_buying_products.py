from playwright.sync_api import Page, expect

from src.pages.overview_page import OverviewPage
from src.pages.your_info_page import YourInfoPage
from src.pages.cart_page import CartPage
from src.pages.inventory_page import InventoryPage
from src.pages.login_page import LoginPage
from src.data.data_text import DataText
from src.config import Config


class TestPurchaseFlow:
    """Тестирование процесса оформления и завершения покупки."""

    def test_complete_purchase_flow(self, custom_page: Page):
        """Проверяет успешное оформление и завершение покупки товара.

        Выполняет полный позитивный сценарий:
        1. Авторизация под стандартным пользователем
        2. Добавление товара в корзину
        3. Переход к оформлению заказа
        4. Заполнение персональных данных
        5. Подтверждение заказа

        Args:
            custom_page: Фикстура страницы Playwright.
        """

        login_page = LoginPage(custom_page)
        inventory_page = InventoryPage(custom_page)
        cart_page = CartPage(custom_page)
        your_info_page = YourInfoPage(custom_page)
        overview_page = OverviewPage(custom_page)

        login_page.navigate_to_login_page()
        login_page.login(DataText.LOGIN_STANDARD_USER, DataText.PASSWORD)

        expect(custom_page).to_have_url(Config.URL_SAUCEDEMO_INVENTORY)

        inventory_page.add_product_to_cart_by_name(DataText.PRODUCT_SAUCE_LABS_BACKPACK)
        inventory_page.click_cart_icon()

        assert DataText.PRODUCT_SAUCE_LABS_BACKPACK in cart_page.get_product_names_in_cart()

        cart_page.click_checkout()
        your_info_page.fill_out_data(DataText.FIRST_NAME, DataText.LAST_NAME, DataText.MAIL_INDEX)
        overview_page.click_finish()

        expect(custom_page).to_have_url(Config.URL_SAUCEDEMO_CHECKOUT_COMPLETE)