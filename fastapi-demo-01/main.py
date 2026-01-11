from fastapi import FastAPI

app = FastAPI(debug=True)


@app.get("/")
def root():
    return {"message": "Hello from docker!!"}


@app.get("/health-check")
def health_check():
    payload = {"status": "Healthy"}
    return payload
