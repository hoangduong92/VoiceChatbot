from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    print("Hello duongbibo")
    return {"message": "Hello World"}