FROM python:3.11-slim

WORKDIR /app

RUN pip install poetry

COPY pyproject.toml poetry.lock* /app/

# No need for virtual environments inside Docker
RUN poetry config virtualenvs.create false && poetry install --no-root

COPY . /app/

EXPOSE 8080

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]