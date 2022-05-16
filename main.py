"""
Author: Prabal Pathak
"""
from fastapi import FastAPI, Request, Response
from fastapi.responses import JSONResponse, StreamingResponse
from fastapi import Depends
from schema import User
from database import UserSchema, engine, Session, Base

Base.metadata.create_all(bind=engine)
app = FastAPI()


@app.get("/")
async def root():
    """ root endpoint """
    return {"Hello": "World"}

@app.post("/new_user")
async def create_user(user: User, response: Response):
    """ create new user """
    user_schema = UserSchema(**user.dict())
    response.status_code = 201
    return {"message": "User created successfully"}

if __name__ == "__main__":
    import uvicorn 
    uvicorn.run(app, port=8000, reload=True)
