FROM ghcr.io/astral-sh/uv:python3.12-alpine

WORKDIR /app

COPY ./pyproject.toml ./uv.lock .python-version ./

RUN uv sync

COPY . .

CMD ["uv", "run", "fastapi", "run", "src/main.py", "--host", "0.0.0.0", "--port", "8000"]