from fastapi import APIRouter,Depends,Form
from sqlalchemy.orm import Session
from app.deps import get_db
from app.models import *


router=APIRouter(tags=["Products"])


@router.get('/get_one_product/{product_id}',description="This Route is for one product at a time")
def get_one_product(product_id:int,db:Session=Depends(get_db)):
    get_data=db.query(Product).filter(Product.id==product_id,Product.status==1).first()
    if not get_data:
        return{"status":0, "msg":"This Product is Currently not available"}
    get_reviews=db.query(Review).filter(Review.product_id==product_id).all()
    if not get_reviews:
        reviews="No reviews available for this product"
    else:
        reviews=[]
        for i in get_reviews:
            reviews.append({
                "rating":i.rating,
                "review":i.review_text
            })
    if get_data.stock_quantity==0:
        stock_quantity="This product is out of stocks"
    else:
        stock_quantity=get_data.stock_quantity
    return{
            "product_name":get_data.product_name,
            "brand_name":get_data.brand,
            "category":get_data.category,
            "description":get_data.description,
            "price":get_data.price,
            "stock_quantity":stock_quantity,
            "rating":get_data.average_rating,
            "user_reviews":reviews      
            }
  