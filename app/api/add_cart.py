from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from app.models import *
from app.deps import get_db

router=APIRouter(tags=["Order Management"])

@router.post("/cart",description="This route is used to add items to the cart")
def add_cart(product_id:int,user_id:int,quantity:int=None,db:Session=Depends(get_db)):
    get_product=db.query(Product).filter(Product.id==product_id,Product.status==1).first()
    if not get_product:
        return{"msg":"That product is not available","status":0}
    if quantity is None:
        quantity=1
    new_item=Cart(
        user_id=user_id,
        product_id=product_id,
        quantity=quantity
    )
    get_cart=db.query(Cart).filter(Cart.product_id==product_id,Cart.user_id==user_id).first()
    if get_cart:
        return{"status":0,"msg":"Product already in cart try increasing the product quantity if you want","data":get_cart.id}
    db.add(new_item)
    db.commit()
    return{"status":1,"msg":"Product Added in the Cart"}
    