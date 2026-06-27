from sqlalchemy import Column, String, Integer, DateTime, ForeignKey, Text, Float
from app.db.base import Base
from datetime import datetime


class Review(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)

    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    rating = Column(Float, nullable=False)
    review_text = Column(Text)