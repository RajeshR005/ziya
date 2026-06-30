from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routers import api_router
from app.api.chat import router as chat_router


app=FastAPI(title="Ziya")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "https://your-vercel-domain.vercel.app"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router)
app.include_router(chat_router, prefix="/ziya")
