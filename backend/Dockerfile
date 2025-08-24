FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

# use environment variable for entrypoint in docker-compose (migrate + run)
CMD ["gunicorn", "insureconnect.wsgi:application", "--bind", "0.0.0.0:8000"]
