from fastapi import FastAPI
from Functions import Return1

app = FastAPI()

@app.get("/result")
async def GetResult():
    return Return1()



# python -m venv venv
# venv\Scripts\activate