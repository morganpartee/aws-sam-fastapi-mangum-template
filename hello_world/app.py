from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()


@app.get("/")
def get_root():
    return {"Hello": "World"}


@app.get("/test")
def get_test():
    return {"hell": "yeah"}

lambda_handler = Mangum(app, lifespan="off")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", port=5000, log_level="info", reload=True)
