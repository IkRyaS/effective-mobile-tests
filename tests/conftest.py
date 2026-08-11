import allure
import pytest
from playwright.sync_api import sync_playwright

from src.config import SaucedemoConfig
from src.api.client import GitHubClient
from src.utils.tools import generate_unique_suffix


@pytest.fixture(scope="function")
def custom_page():
    """Создает и возвращает страницу Playwright для автоматизации браузера.

    Returns:
        Page: Объект страницы Playwright для взаимодействия с браузером.
    """
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=SaucedemoConfig.HEADLESS)
        page = browser.new_page()
        yield page
        browser.close()


@pytest.fixture()
def github_client() -> GitHubClient:
    """Создает и возвращает авторизованный клиент GitHub API.

    Returns:
        Экземпляр GitHubClient со стандартным токеном из конфигурации.
    """
    return GitHubClient()


@pytest.fixture()
def temp_repo(github_client: GitHubClient) -> str:
    """Генерирует уникальное имя репозитория и гарантирует его удаление после теста.

    Args:
        github_client: Авторизованный клиент для взаимодействия с API.

    Yields:
        Строку с уникальным сгенерированным именем репозитория.
    """
    repo_name = f"repo_{generate_unique_suffix()}"
    yield repo_name

    with allure.step(f"Пост-условие: Автоматическое удаление репозитория {repo_name}"):
        delete_response = github_client.delete_repo(repo_name)
        if delete_response.status_code not in [204, 307, 403, 404, 409]:
            raise RuntimeError(
                f"Не удалось удалить временный репозиторий в teardown. "
                f"Статус: {delete_response.status_code}, Ответ: {delete_response.text}"
            )
