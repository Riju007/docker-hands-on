from fastapi import FastAPI
import os
import socket

app = FastAPI()


@app.get("/")
def root():
    return {"status": "Healthy"}


@app.get("/env")
def show_env():
    return {"env": dict(os.environ)}


@app.get("/whoami")
def whoami():
    hostname = socket.gethostname()
    return {"host_name": hostname}
