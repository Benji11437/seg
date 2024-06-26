# Utilisez une image de base officielle pour Python
FROM python:3.9-slim


WORKDIR /app

COPY requirements.txt /app

RUN pip install -r requirements.txt

COPY . /app

EXPOSE 8501

CMD ["streamlit","run","app.py","--host", "0.0.0.0","--port","8000"]