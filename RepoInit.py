from fastapi import FastAPI
from Functions import Return1

app = FastAPI()

@app.get("/result")
async def GetResult():
    return Return1()


# poetry run fastapi dev RepoInit.py 