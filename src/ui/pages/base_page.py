from playwright.sync_api import Page, Response


class BasePage:
    """Базовый класс для всех страниц приложения."""

    def __init__(self, page: Page) -> None:
        """Инициализирует базовую страницу.

        Args:
            page: Объект страницы Playwright.
        """
        self.page: Page = page

    def open(self, url: str) -> Response | None:
        """Открывает указанный URL в браузере.

        Args:
            url: Адрес страницы для открытия.

        Returns:
            Response | None: Объект ответа сервера или None, если ответ не получен.

        Raises:
            PlaywrightError: Если произошла ошибка при навигации.
            TimeoutError: Если страница не загрузилась в течение таймаута.
        """
        return self.page.goto(url)