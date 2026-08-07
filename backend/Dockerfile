FROM python:3.12-slim

ARG REQUIREMENTS_FILE=requirements-container.txt

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PATH="/opt/assetmanager-venv/bin:${PATH}"

WORKDIR /app

RUN apt-get update \
    && apt-get install --no-install-recommends -y build-essential curl \
    && rm -rf /var/lib/apt/lists/* \
    && python -m venv /opt/assetmanager-venv

COPY requirements*.txt ./
RUN pip install --no-cache-dir -r "${REQUIREMENTS_FILE}"

COPY app ./app
COPY services ./services

CMD ["uvicorn", "app.main:sio_app", "--host", "0.0.0.0", "--port", "8282"]
