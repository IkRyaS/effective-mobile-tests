# Автоматизированное тестирование интернет-магазина и GitHub API

Проект содержит комплекс тестовых сценариев для проверки сквозного UI-функционала интернет-магазина (Saucedemo) и верификации интеграционных сценариев работы с GitHub REST API.

## Стек технологий

* **Язык программирования:** Python 3.11+
* **UI Автоматизация:** Playwright (Python)
* **API Автоматизация:** Requests
* **Тестовый фреймворк:** Pytest
* **Менеджер пакетов и окружения:** [Astral UV](https://docs.astral.sh/uv/)
* **Отчетность:** Allure Framework
* **Контейнеризация:** Docker / Docker Compose

## Полезные ссылки
* [ТЗ](https://solvit.space/test-tasks/47)
* [Официальная документация GitHub REST API](https://github.com) — спецификация эндпоинтов и форматов ответов.
* [Инструкция по созданию Personal Access Token (PAT)](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens) — пошаговый гайд по генерации Fine-grained и Classic токенов.
* [Руководство по установке Astral UV](https://docs.astral.sh/uv/getting-started/installation/) — официальные скрипты установки для Windows, macOS и Linux.

---

## Предварительные требования

Перед запуском убедитесь, что в вашей системе установлены:
1. Docker Desktop и Docker Compose.
2. Локально (опционально, для запуска без Docker): Python и утилита `uv`.

### Установка UV
```bash
# macOS / Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows (PowerShell)
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

## Настройка окружения

### 1. Клонируйте репозиторий
```bash
git clone https://github.com/IkRyaS/effective-mobile-tests.git
cd effective-mobile-tests
```

### 2. Создайте файл `.env`
Создайте файл `.env` в корневом каталоге проекта со следующими переменными:

```env
SAUCEDEMO_LOGIN=https://www.saucedemo.com/
SAUCEDEMO_INVENTORY=https://www.saucedemo.com/inventory.html
SAUCEDEMO_CHECKOUT_COMPLETE=https://www.saucedemo.com/checkout-complete.html

HEADLESS=true

GITHUB_API_BASE_URL=https://api.github.com
GITHUB_API_TOKEN=ваш_персональный_токен_github
GITHUB_USERNAME=ваш_логин_github
```

---

## Инструкция по запуску

### Вариант 1. Запуск через Docker Compose (Рекомендуемый)

Сборка контейнера и запуск всех тестов (UI и API) в изолированном окружении:
```bash
docker-compose up --build
```

После завершения тестов контейнер автоматически остановится. Артефакты тестов и Allure-результаты сохранятся в локальную папку благодаря настроенным `volumes`.

### Вариант 2. Локальный запуск (Без Docker)

1. Установите зависимости и синхронизируйте виртуальное окружение:
   ```bash
   uv sync
   ```
2. Установите необходимые браузеры Playwright:
   ```bash
   uv run playwright install
   ```
3. Запустите тесты с генерацией Allure-результатов:
   ```bash
   uv run pytest --alluredir=allure-results
   ```

---

## Генерация и просмотр отчетов Allure

Для локального формирования красивого веб-отчета из собранных результатов выполните команду (требуется установленный CLI Allure):
```bash
allure serve allure-results
```
