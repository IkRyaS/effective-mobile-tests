import allure
from playwright.sync_api import Page, expect

from src.ui.pages.overview_page import OverviewPage
from src.ui.pages.your_info_page import YourInfoPage
from src.ui.pages.cart_page import CartPage
from src.ui.pages.inventory_page import InventoryPage
from src.ui.pages.login_page import LoginPage
from src.data.data_text import DataText
from src.config import SaucedemoConfig


@allure.epic("UI тесты")
@allure.feature("Оформление заказа")
@allure.story("Сквозной сценарий покупки")
class TestPurchaseFlow:
    """Тестирование процесса оформления и завершения покупки."""

    @allure.title("Успешное прохождение полного цикла покупки товара")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_complete_purchase_flow(self, custom_page: Page):
        """Проверяет успешное оформление и завершение покупки товара.

        Args:
            custom_page: Фикстура страницы Playwright.
        """
        login_page = LoginPage(custom_page)
        inventory_page = InventoryPage(custom_page)
        cart_page = CartPage(custom_page)
        your_info_page = YourInfoPage(custom_page)
        overview_page = OverviewPage(custom_page)

        with allure.step("Перейти на страницу авторизации"):
            login_page.navigate_to_login_page()

        with allure.step(f"Выполнить вход под пользователем: {DataText.LOGIN_STANDARD_USER}"):
            login_page.login(DataText.LOGIN_STANDARD_USER, DataText.PASSWORD)

        with allure.step("Проверить успешный переход на страницу каталога товаров"):
            expect(custom_page).to_have_url(SaucedemoConfig.URL_SAUCEDEMO_INVENTORY)

        with allure.step(f"Добавить товар '{DataText.PRODUCT_SAUCE_LABS_BACKPACK}' в корзину"):
            inventory_page.add_product_to_cart_by_name(DataText.PRODUCT_SAUCE_LABS_BACKPACK)

        with allure.step("Перейти в корзину покупок"):
            inventory_page.click_cart_icon()

        with allure.step(f"Проверить наличие товара '{DataText.PRODUCT_SAUCE_LABS_BACKPACK}' в корзине"):
            assert DataText.PRODUCT_SAUCE_LABS_BACKPACK in cart_page.get_product_names_in_cart()

        with allure.step("Нажать на кнопку оформления заказа (Checkout)"):
            cart_page.click_checkout()

        with allure.step(f"Заполнить персональные данные: {DataText.FIRST_NAME}, {DataText.LAST_NAME}, {DataText.MAIL_INDEX}"):
            your_info_page.fill_out_data(DataText.FIRST_NAME, DataText.LAST_NAME, DataText.MAIL_INDEX)

        with allure.step("Подтвердить и завершить оформление заказа"):
            overview_page.click_finish()

        with allure.step("Проверить успешный переход на финальную страницу завершения заказа"):
            expect(custom_page).to_have_url(SaucedemoConfig.URL_SAUCEDEMO_CHECKOUT_COMPLETE)
