from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "ring_backend is running"}