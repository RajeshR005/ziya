from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from app.models import *
from app.deps import get_db

router=APIRouter(tags=["Order Management"])

@router.post('/cart_update',description="This Route is for Updating the items in the cart")
def update_cart(cart_item_id:int,quantity:int,user_id:int=1,db:Session=Depends(get_db)):
    get_cart_data=db.query(Cart).filter(Cart.id==cart_item_id,Cart.user_id==user_id).first()
    if not get_cart_data:
        return{"status":0,"msg":"This item is not exist in the cart try adding again"}
    if quantity<=0:
        db.delete(get_cart_data)
        db.commit()

        return {
            "status": 1,
            "msg": "Item removed from cart."
        }
    get_cart_data.quantity=quantity
    db.commit()
    return{"status":1,"msg":"Item updated Successfully"}