from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from app.deps import get_db
from app.models import *


router=APIRouter(tags=["Products"])


@router.get('/get_all_products',description="This Route is for getting all the products")
def get_products_all(db:Session=Depends(get_db)):
    products_li=[]
    get_data=db.query(Product).filter(Product.status==1).all()
    if not get_data:
        return{"status":0, "msg":"No products available"}
    for i in get_data:
        products_li.append({
            "product_name":i.product_name,
            "brand_name":i.brand,
            "category":i.category,
            "description":i.description,
            "price":i.price,
            "stock_quantity":i.stock_quantity,
            "rating":i.average_rating        
            })
    return products_li