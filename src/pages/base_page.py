from playwright.sync_api import Page, Response


class BasePage:

    def __init__(self, page: Page):
        self.page = page

    def open(self, url: str) -> Response | None:
        """Открыть указанный URL."""
        return self.page.goto(url)