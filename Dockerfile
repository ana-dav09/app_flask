# Imagen base de Python
FROM python:3.11-slim

# Directorio
WORKDIR /app

COPY requirements.txt .
COPY app.py .
COPY templates/ ./templates/

# Dependencias
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["python", "app.py"]
