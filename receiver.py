from fastapi import FastAPI

app = FastAPI()

@app.post("/execute_command")
async def execute_command(command: dict):
    if command:
        print("Received Message: ", command)
    return {"status": "success"}
