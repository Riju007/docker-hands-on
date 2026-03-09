from fastapi import FastAPI
import os

app = FastAPI()


@app.get("/")
def root():
    return {"status": "Healthy"}


@app.get("/env")
def show_env():
    return {"env": dict(os.environ)}
