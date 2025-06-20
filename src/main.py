from fastapi import FastAPI

app = FastAPI(title="Task Manah=ger API")


@app.get("/")
async def read_root():
  return {"message": "Hello, World!"}