from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routers import api_router


app=FastAPI(title="Ziya")

@app.get("/")
def home():
    return {
        "project": "Ziya – AI Shopping Assistant",
        "description": (
            "An Agentic AI-powered shopping assistant that enables "
            "natural language product discovery, intelligent recommendations, "
            "product comparison, conversational shopping, JWT-based authentication, "
            "and cart management."
        ),
        "status": "Running",
        "version": "1.0.0",
        "developer": "Rajesh R",
        "frontend": "https://ziya-ecru.vercel.app/",
        "backend": "https://ziya-backend.onrender.com/",
        "documentation": "https://ziya-backend.onrender.com/docs",
        "github": "https://github.com/RajeshR005/ziya",
        "tech_stack": {
            "backend": [
                "FastAPI",
                "Python",
                "MySQL",
                "SQLAlchemy",
                "Alembic",
                "JWT Authentication"
            ],
            "ai": [
                "LangChain",
                "LangGraph",
                "Groq (Qwen3-27B)",
                "Agentic AI"
            ]
        },
        "features": [
            "Natural language product search",
            "Product filtering",
            "Product comparison",
            "Detailed product reviews",
            "AI conversational shopping assistant",
            "JWT authentication",
            "Shopping cart management",
            "Conversation memory",
            "REST API"
        ]
    }

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "https://ziya-ecru.vercel.app"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router)

