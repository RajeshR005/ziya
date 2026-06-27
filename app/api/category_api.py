from fastapi import FastAPI,APIRouter,Depends
from sqlalchemy.orm import Session
from app.models import *
from app.deps import get_db

router=APIRouter(tags=["Category"])

@router.get('/categories',description="This Route is for Categories")
def get_categories(db:Session=Depends(get_db)):
    categories=db.query(Product.category).distinct().all()
    cat=[]
    for i in categories:
            cat.append(i.category)
    return cat
