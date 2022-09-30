from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()


@app.get("/main")
def read_root():
    return {"Hello": "World"}


@app.get("/test")
def read_item():
    return {"hell": "yeah"}

lambda_handler = Mangum(app, lifespan="off")
