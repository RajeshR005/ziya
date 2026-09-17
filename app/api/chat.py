from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from typing import Optional
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain.agents import create_agent
from langgraph.checkpoint.memory import InMemorySaver
from ziya.tools import get_all_brands,get_all_categories,filter_products, one_product_details, manage_cart_items, show_orders, login
from ziya.prompts import system_prompt

load_dotenv()

router = APIRouter(tags=["Chat"])

# Shared memory for all chat sessions
memory = InMemorySaver()

llm = ChatGroq(model="openai/gpt-oss-120b")



agent = create_agent(
    llm,
    tools=[get_all_categories,get_all_brands,filter_products, one_product_details, manage_cart_items, show_orders],
    checkpointer=memory,
    system_prompt=system_prompt,
)


class ChatRequest(BaseModel):
    message: str
    thread_id: str
    access_token: Optional[str] = None


class ChatResponse(BaseModel):
    reply: str
    thread_id: str


@router.post("/chat", description="Chat with the Ziya AI Shopping Assistant")
def chat(request: ChatRequest):
    try:
        config = {"configurable": {"thread_id": request.thread_id}}
        user_message = request.message
        if request.access_token:
            import ziya.tools.auth_tool as auth_tool
            auth_tool.ACCESS_TOKEN = request.access_token
            user_message = f"[SYSTEM: User is ALREADY authenticated. DO NOT use the login tool. Proceed directly with the requested tool.] {request.message}"
        else:
            import ziya.tools.auth_tool as auth_tool
            auth_tool.ACCESS_TOKEN = None

        result = agent.invoke(
            {"messages": {"role": "user", "content": user_message}},
            config=config,
        )

        reply = result["messages"][-1].content

        return ChatResponse(reply=reply, thread_id=request.thread_id)

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Chat error: {str(e)}")
