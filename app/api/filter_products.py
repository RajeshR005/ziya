from fastapi import APIRouter,Depends,Form
from sqlalchemy.orm import Session
from sqlalchemy import and_, or_
from app.deps import get_db
from app.models import *


router=APIRouter(tags=["Products"])


@router.get('/filter_products/',description="This Route is for one product at a time")
def get_one_product(brand:str=None,category:str=None,min_price:float=None,max_price:float=None,min_rating:float=None,max_rating:float=None,db:Session=Depends(get_db)):
    get_data=db.query(Product).filter(Product.status==1)
    products_li=[]
    if not get_data:
        return{"status":0, "msg":"No products available"}
    if brand is not None:
        get_data=get_data.filter(Product.brand==brand)
    if category is not None:
        get_data=get_data.filter(Product.category==category)
    if min_price or max_price is not None:
        if min_price and max_price:
            get_data=get_data.filter(and_(Product.price>=min_price,Product.price<=max_price))
        elif min_price:
            get_data=get_data.filter(Product.price>=min_price)
        else:
            get_data=get_data.filter(Product.price<=max_price)
    if min_rating or max_rating is not None:
        if min_rating and max_rating:
            get_data=get_data.filter(and_(Product.average_rating>=min_rating,Product.average_rating<=max_rating))
        elif min_rating:
            get_data=get_data.filter(Product.average_rating>=min_rating)
        else:
            get_data=get_data.filter(Product.average_rating<=max_rating)
    products_data=get_data.all()
    for i in products_data:
        products_li.append({
            "product_id":i.id,
            "product_name":i.product_name,
            "brand_name":i.brand,
            "category":i.category,
            "description":i.description,
            "price":i.price,
            "stock_quantity":i.stock_quantity,
            "rating":i.average_rating        
            })
    return products_li