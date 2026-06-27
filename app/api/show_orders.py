from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from app.deps import get_db
from app.models import *

router=APIRouter(tags=["Order Management"])

@router.get('/get_cart',description="This Route is for getting the items from the cart")
def get_cart(user_id:int,db:Session=Depends(get_db)):
    get_data=db.query(Cart).filter(Cart.user_id==user_id).all()
    if not get_data:
        return{"status":0,"msg":"There is no items in the Cart go explore products"}
    cart_li=[]
    un_avil=[]
    total_cart_value=0
    for i in get_data:
        get_product=db.query(Product).filter(Product.id==i.product_id,Product.status==1).first()
        if not get_product:
            un_avil.append({
                "product_name":get_product.product_name,
                "Availability":"Not Available"
            })
        else:
            cart_li.append({
                "product_name":get_product.product_name,
                "brand":get_product.brand,
                "price":get_product.price,
            })
            total_cart_value+=get_product.price

    return{
        "products":cart_li,
        "total_cart_value":total_cart_value

    }