from fastapi import FastAPI

app = FastAPI()


@app.get("/user/items")
async def root():
    return [""]