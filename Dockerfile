# Dockerfile - Como fazer uma caixinha com seu app

# Começa com Python (a base)
FROM python:3.11-slim

# Copia seus arquivos pra dentro da caixinha
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY app.py .
COPY tests.py .

# O que rodar quando a caixinha iniciar
CMD ["python", "app.py"]