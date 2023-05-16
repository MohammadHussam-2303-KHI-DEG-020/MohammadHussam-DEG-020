FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

ENV FLASK_ENV=production
ENV TODO_DB=/app/todo.db

EXPOSE 5000

CMD ["python", "main.py"]
