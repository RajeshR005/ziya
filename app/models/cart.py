from sqlalchemy import Column, String, Integer, DateTime, ForeignKey, Text, Float
from app.db.base import Base
from datetime import datetime

class Cart(Base):
    __tablename__ = "cart"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    product_id = Column(Integer, ForeignKey("products.id"))
    quantity = Column(Integer, default=1)