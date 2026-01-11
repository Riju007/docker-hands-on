FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt /app/

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

# CMD ["uvicorn","main:app","--reload","--reload-dir","/app","--host","0.0.0.0","--port","8000"]
CMD ["uvicorn","main:app","--reload","--host","0.0.0.0","--port","8000"]