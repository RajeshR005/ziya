from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routers import api_router


app=FastAPI(title="Ziya")

@app.get("/")
def home():
    return {
        "project": "Ziya AI Shopping Assistant",
        "description": "An AI-powered shopping assistant that enables product discovery, conversational search, cart management, and JWT-based authentication using an agentic workflow.",
        "tech_stack": [
            "FastAPI",
            "LangChain",
            "LangGraph",
            "Groq",
            "MySQL",
            "JWT Authentication"
        ],
        "status": "Running",
        "version": "1.0.0",
        "documentation": "/docs",
        "github": "https://github.com/RajeshR005/ziya",
        "developer": "Rajesh R"
    }

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "https://your-vercel-domain.vercel.app"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router)

