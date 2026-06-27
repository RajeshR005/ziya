from sqlalchemy import Column,String,Integer,DateTime,Date,ForeignKey
from app.db.base import Base
from datetime import date,datetime,time

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    first_name = Column(String(100))
    last_name = Column(String(100))
    date_of_birth = Column(Date)
    email = Column(String(100), index=True, nullable=False)
    password = Column(String(300), nullable=False)
    phone_number = Column(String(50), nullable=True)
    status=Column(Integer,default=1)
    role=Column(String(50),default="user")
    created_at = Column(DateTime,default=datetime.now)
    created_by=Column(Integer,ForeignKey('users.id'))
    modified_at=Column(DateTime,default=datetime.now,onupdate=datetime.now)
    modified_by=Column(Integer,ForeignKey('users.id'))
