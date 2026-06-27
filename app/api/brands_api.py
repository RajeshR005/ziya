from fastapi import FastAPI,APIRouter,Depends
from sqlalchemy.orm import Session
from app.models import *
from app.deps import get_db

router=APIRouter(tags=["Brands"])

@router.get('/brands',description="This Route is for Brand")
def get_categories(db:Session=Depends(get_db)):
    brands=db.query(Product.brand).distinct().all()
    cat=[]
    for i in brands:
            cat.append(i.brand)
    return cat
