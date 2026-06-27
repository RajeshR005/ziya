from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from app.models import *
from app.deps import get_db

router=APIRouter(tags=["Reviews"])

@router.post('/get_reviews',description="This is Route to get the reviews for the products")
def get_reviews(reviews_li:list[int],db:Session=Depends(get_db)):
    get_revs=db.query(Review).filter(Review.product_id.in_(reviews_li)).all()
    reviews=[]
    for i in get_revs:
        reviews.append({
            "product_id":i.product_id,
            "review":i.review_text,
            "rating":i.rating
        })
    return reviews
