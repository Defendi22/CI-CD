# Dockerfile - FastAPI com Uvicorn

FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY app.py .
COPY tests.py .

# ✅ Expõe a porta do FastAPI
EXPOSE 8000

# ✅ Uvicorn inicia o FastAPI (não python app.py)
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]