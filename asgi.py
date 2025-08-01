from fastapi import FastAPI
from user.main import create_app

app: FastAPI = create_app()
# uv run uvicorn --factory user.main:create_app
# uv run uvicorn asgi:app
# uv run fastapi dev asgi.py
