#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Database connection and Base decleartion
Author: Prabal Pathak
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Boolean
from datetime import datetime

__all__ = ['db', 'Base', 'Session']

url = 'sqlite:///database.db' # sqlite:///:memory: or sqlite:///relative/path/to/file.db
engine = create_engine(url, echo=False) # echo=True for debugging
Session = sessionmaker(bind=engine) # bind=engine for sqlite optional: autocommit=False, autoflush=False
Base = declarative_base() # Base class for all tables

def db():
    """
    Yield a session object
    """
    session = Session()
    try:
        yield session
    finally:
        session.close()
