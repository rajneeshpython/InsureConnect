FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

# install system deps (postgres + redis cli + netcat)
RUN apt-get update && apt-get install -y \
    postgresql-client \
    redis-tools \
    netcat-openbsd \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app
RUN chmod +x /app/wait_for_db.sh

CMD ["gunicorn", "insureconnect.wsgi:application", "--bind", "0.0.0.0:8000"]
