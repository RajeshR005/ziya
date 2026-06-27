from app.db.session import SessionLocal
from sqlalchemy.orm import Session
from typing import Generator
from dotenv import load_dotenv
import os

load_dotenv()

def get_db() -> Generator:
       
        try:
            db = SessionLocal()
            yield db
        finally:
            db.close()
