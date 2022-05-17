#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import List, Optional, Dict
from datetime import datetime
from pydantic import BaseModel, EmailStr

class User(BaseModel):
    username: str
    email: EmailStr
    password: int
    is_admin: bool
    is_active: bool
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()
    updated_by : Optional[str] = None
    additional_info: Optional[str] = None

    class Config:
        orm_mode = True


if __name__ == '__main__':
    user = {
        'id': 1,
        'username': 'John Doe',
        'email': 'prabal@gmail.com',
        'password': '232',
        'is_admin': True,
        'is_active': True,
        'additional_info': "age: 23"
    }
    user_model = User(**user)
    print(user_model.dict())
    print(user_model)
