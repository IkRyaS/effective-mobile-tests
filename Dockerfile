FROM mcr.microsoft.com/playwright/python:latest
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/
WORKDIR /app
COPY pyproject.toml uv.lock ./
RUN uv sync --frozen
COPY src/ ./src
COPY tests/ ./tests
RUN uv run playwright install
CMD ["uv", "run", "pytest"]