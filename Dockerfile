FROM mcr.microsoft.com/playwright/python:latest

RUN pip install uv

WORKDIR /app

COPY pyproject.toml uv.lock ./

RUN uv sync --frozen --no-install-project

COPY src/ ./src
COPY tests/ ./tests

RUN uv run playwright install chromium --with-deps && \
    uv cache clean && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

ENV PATH="/app/.venv/bin:$PATH"

ENV PLAYWRIGHT_BROWSERS_PATH=/ms-playwright

CMD ["pytest", "--alluredir=allure-results", "-v"]