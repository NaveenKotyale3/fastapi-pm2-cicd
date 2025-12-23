from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello from FastAPI v1"}

@app.get("/version")
def version():
    return {"version": "v6"}


@app.get("/health")
def health():
    return {"status":"everything working fine"}