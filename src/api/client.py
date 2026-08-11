from typing import Optional

import allure
import requests

from src.config import GitHubConfig


class GitHubClient:
    """Клиент для взаимодействия с GitHub REST API.

    Предоставляет методы для управления репозиториями, автоматической
    настройки заголовков авторизации и выполнения HTTP-запросов.
    """

    def __init__(self, token: Optional[str] = None):
        """Инициализирует сессию GitHub клиента.

        Args:
            token: Персональный токен доступа (PAT). Если не передан,
                используется токен по умолчанию из конфигурации.
        """
        self.token = token if token else GitHubConfig.GITHUB_API_TOKEN
        self.base_url = GitHubConfig.URL_GITHUB
        self.username = GitHubConfig.GITHUB_USERNAME
        self.session = requests.Session()
        self._set_headers()

    def _set_headers(self):
        """Устанавливает обязательные заголовки авторизации и версии API в сессию."""
        headers = {
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2026-03-10"
        }
        if self.token:
            headers["Authorization"] = f"Bearer {self.token}"

        self.session.headers.update(headers)

    def _requests(self, method: str, endpoint: str, **kwargs) -> requests.Response:
        """Внутренний метод для отправки HTTP-запросов через базовую сессию.

        Args:
            method: Метод HTTP-запроса (например, "GET", "POST").
            endpoint: Относительный путь эндпоинта API (например, "/user").
            **kwargs: Дополнительные параметры для передачи в requests.request.

        Returns:
            Объект ответа requests.Response от API GitHub.
        """
        url = f"{self.base_url.rstrip('/')}{endpoint}"
        response = self.session.request(method, url, **kwargs)
        return response

    @allure.step("Получение списка публичных репозиториев пользователя")
    def get_public_repo_list(self, **kwargs) -> requests.Response:
        """Возвращает список публичных репозиториев заданного пользователя.

        Args:
            **kwargs: Дополнительные query-параметры запроса.

        Returns:
            Объект ответа requests.Response со списком репозиториев в JSON.
        """
        return self._requests("GET", f"/users/{self.username}/repos", **kwargs)

    @allure.step("Создание репозитория")
    def create_repo(self, name: str, description: Optional[str] = None,
                    private: Optional[bool] = False, has_issues: Optional[bool] = True,
                    has_projects: Optional[bool] = True, has_wiki: Optional[bool] = True,
                    ) -> requests.Response:
        """Создает новый репозиторий для авторизованного пользователя.

        Args:
            name: Имя создаваемого репозитория.
            description: Описание репозитория. По умолчанию None.
            private: Флаг приватности (True для приватного). По умолчанию False.
            has_issues: Включить ли раздел Issues. По умолчанию True.
            has_projects: Включить ли раздел Projects. По умолчанию True.
            has_wiki: Включить ли раздел Wiki. По умолчанию True.

        Returns:
            Объект ответа requests.Response со статусом 201 в случае успеха.
        """
        payload = {
            "name": name,
            "private": private,
            "has_issues": has_issues,
            "has_projects": has_projects,
            "has_wiki": has_wiki
        }
        if description:
            payload["description"] = description

        allure.attach(name, name="Имя создаваемого репозитория", attachment_type=allure.attachment_type.TEXT)
        return self._requests("POST", "/user/repos", json=payload)

    @allure.step("Удаление репозитория")
    def delete_repo(self, name: str, **kwargs) -> requests.Response:
        """Удаляет указанный репозиторий пользователя.

        Args:
            name: Имя удаляемого репозитория.
            **kwargs: Дополнительные параметры запроса.

        Returns:
            Объект ответа requests.Response со статусом 204 в случае успеха.
        """
        allure.attach(name, name="Имя удаляемого репозитория", attachment_type=allure.attachment_type.TEXT)
        return self._requests("DELETE", f"/repos/{self.username}/{name}", **kwargs)