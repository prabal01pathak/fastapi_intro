"""
Author: Prabal Pathak
"""
from fastapi import FastAPI


app = FastAPI()


@app.get("/")
async def root():
    """ root endpoint """
    return {"Hello": "World"}


if __name__ == "__main__":
    import uvicorn 
    uvicorn.run(app, port=8000)
