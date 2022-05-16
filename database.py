#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Boolean
from datetime import datetime

url = 'sqlite:///database.db'
engine = create_engine(url, echo=True)
Session = sessionmaker(bind=engine)
Base = declarative_base()

class UserSchema(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)
    email = Column(String, unique=True)
    is_admin = Column(Boolean, default=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    updated_by = Column(String)
    additional_info = Column(String)

    def __init__(
            self, username, password, 
            email, is_admin, is_active, 
            created_at, updated_at, updated_by, 
            additional_info
    ):
        self.username = username
        self.password = password
        self.email = email
        self.is_active = is_active
        self.is_admin = is_admin
        self.created_at = created_at
        self.updated_at = updated_at
        self.updated_by = updated_by

    def __repr__(self):
        return "<User('%s','%s','%s')>" % (self.username, self.password, self.email)
