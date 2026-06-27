from sqlalchemy import Column, String, Integer, DateTime, ForeignKey, Text, Float
from app.db.base import Base
from datetime import datetime


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)

    product_name = Column(String(255), nullable=False, index=True)
    brand = Column(String(100))
    category = Column(String(100))

    description = Column(Text)

    price = Column(Float, nullable=False)
    stock_quantity = Column(Integer, default=0)

    average_rating = Column(Float, default=0.0)

    status = Column(Integer, default=1)