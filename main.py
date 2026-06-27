from fastapi import FastAPI
from app.api.routers import api_router


app=FastAPI(title="Ziya")



app.include_router(api_router)
