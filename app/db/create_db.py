from sqlalchemy import create_engine,text
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL=os.getenv("DATABASE_URL")
DATABASE_NAME="ziya"

engine=create_engine(DATABASE_URL)

def create_db():
    with engine.connect() as conn:
        conn.execute(text(F"CREATE DATABASE IF NOT EXISTS {DATABASE_NAME}"))
        print(f"Database Created Successfully: {DATABASE_NAME}")

if __name__=="__main__":
    create_db()

