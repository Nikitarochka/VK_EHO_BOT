# Dockerfile
FROM python:3.10-slim

# устанавливаем рабочую директорию
WORKDIR /app

# копируем файл зависимостей и устанавливаем их
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# копируем исходный код проекта
COPY . .

# запускаем приложение как модуль
CMD ["python", "-m", "app.main"]
