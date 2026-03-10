# 📝 Task Manager API — FastAPI 

API simples de tarefas com FastAPI, testes automatizados e CI/CD.

## 🚀 Como rodar

```bash
# Instalar dependências
pip install -r requirements.txt

# Rodar o servidor
uvicorn app:app --reload
```

Acesse: http://localhost:8000/docs (Swagger automático do FastAPI)

## 🧪 Rodar os testes

```bash
pytest test_app.py -v --cov=app
```

## 📦 Endpoints

| Método | Rota             | Descrição         |
|--------|------------------|-------------------|
| GET    | /tasks           | Listar todas      |
| GET    | /tasks/{id}      | Buscar por ID     |
| POST   | /tasks           | Criar tarefa      |
| PUT    | /tasks/{id}      | Atualizar tarefa  |
| DELETE | /tasks/{id}      | Deletar tarefa    |

## ⚙️ CI/CD

O pipeline `.github/workflows/ci.yml` roda automaticamente no push:
1. Instala dependências
2. Roda os testes com cobertura
3. Faz deploy (quando na branch `main`)