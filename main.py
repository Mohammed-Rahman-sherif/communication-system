from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def execute_command():
    return {"status": "success"}
