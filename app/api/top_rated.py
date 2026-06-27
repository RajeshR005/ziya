from fastapi import FastAPI,APIRouter,Depends
from sqlalchemy.orm import Session
from app.models import *
from app.deps import get_db

router=APIRouter(tags=["Top-Rated"])

@router.get('/top_rated',description="This Route is for Brand")
def top_rated_products(db:Session=Depends(get_db)):
    top_rated=db.query(Product).filter(Product.average_rating>=4.5).all()
    if not top_rated:
        return{"msg":"No Top Rated Products"}
    top=[]
    for i in top_rated:
        top.append({
            "product_name":i.product_name,
            "brand_name":i.brand,
            "category":i.category,
            "description":i.description,
            "price":i.price,
            "stock_quantity":i.stock_quantity,
            "rating":i.average_rating        
            })
    return top
