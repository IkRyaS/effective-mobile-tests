import allure

from src.api.client import GitHubClient


@allure.epic("API тесты")
@allure.feature("Управление репозиториями")
@allure.story("Создание публичного репозитория")
class TestCreateNewPublicRepository:
    """Набор тестов для проверки создания публичных репозиториев через GitHub API."""

    @allure.title("Успешное создание и верификация публичного репозитория")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_success_create_new_public_repo(self, github_client: GitHubClient, temp_repo: str):
        """Позитивный сценарий создания публичного репозитория.

        Args:
            github_client: Авторизованный клиент для работы с GitHub API.
            temp_repo: Уникальное имя временного репозитория из фикстуры.
        """
        with allure.step(f"Отправить POST-запрос на создание репозитория: {temp_repo}"):
            create_response = github_client.create_repo(temp_repo)
            assert create_response.status_code == 201

        with allure.step("Отправить GET-запрос для получения списка репозиториев пользователя"):
            info_response = github_client.get_public_repo_list()
            assert info_response.status_code == 200

        with allure.step(f"Проверить наличие созданного репозитория {temp_repo} в полученном списке"):
            repo_names_list = [repo["name"] for repo in info_response.json()]
            assert temp_repo in repo_names_list

    @allure.title("Отклонение запроса на создание репозитория без токена авторизации")
    @allure.severity(allure.severity_level.NORMAL)
    def test_create_repo_without_auth_denied(self, temp_repo: str):
        """Проверка невозможности создания репозитория неавторизованным клиентом.

        Args:
            temp_repo: Уникальное имя временного репозитория из фикстуры.
        """
        with allure.step("Инициализировать клиент GitHub с некорректным токеном авторизации"):
            unauthorized_client = GitHubClient(token="invalid_or_empty_token_string")

        with allure.step(f"Отправить POST-запрос на создание репозитория {temp_repo} без авторизации"):
            create_response = unauthorized_client.create_repo(temp_repo)
            assert create_response.status_code == 401
