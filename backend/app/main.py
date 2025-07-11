from fastapi import FastAPI

app = FastAPI(
    title="Backend test"
) 

@app.get("/")
def read_root():
    return {"Hello": "World"}

