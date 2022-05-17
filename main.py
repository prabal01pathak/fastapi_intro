"""
description: main file for the project "Run: uvicorn main:app --reload" --> Optional[host, port, reload]
Author: Prabal Pathak
"""
from fastapi import FastAPI, Request, Response
from fastapi.responses import JSONResponse, StreamingResponse
from fastapi import Depends
from database import database, schema, models
from database.database import db, Session

database.Base.metadata.create_all(bind=database.engine) # create all tables
app = FastAPI()


@app.get("/")
async def root()->JSONResponse:
    """ root endpoint 
    return : "message"
    """
    return {"message": "Hello World"}


@app.post("/new_user")
async def create_user(user: schema.User,response: Response, db: Session = Depends(db))->JSONResponse:
    """ 
    create new user 
    args: user: schema.User, response: Response, db: Session = Depends(db)
    return: JSONResponse
    """
    user_schema = models.UserSchema(**user.dict())
    db.add(user_schema)
    db.commit()
    response.status_code = 201
    return {"message": "User created successfully"}


if __name__ == "__main__":
    """
    run the application as:
    python3 main.py
    """
    import uvicorn 
    uvicorn.run(app, port=8000)
