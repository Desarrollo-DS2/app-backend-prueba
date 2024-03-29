FROM python:3.9-alpine

RUN apk update && \
    apk add --no-cache \
        ca-certificates gcc postgresql-dev linux-headers musl-dev \
        libffi-dev jpeg-dev zlib-dev \
        git bash

WORKDIR /app

ENV PYTHONUNBUFFERED 1

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["python", "/app/manage.py", "runserver", "0.0.0.0:8000"]