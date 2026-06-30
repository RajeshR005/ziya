"""
Chat API endpoint for the Ziya frontend.
This is a NEW endpoint — does NOT modify any existing backend functionality.
"""

from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from typing import Optional
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain.agents import create_agent
from langgraph.checkpoint.memory import InMemorySaver
from ziya.tools import filter_products, one_product_details, manage_cart_items, show_orders, login
from ziya.prompts import system_prompt

load_dotenv()

router = APIRouter(tags=["Chat"])

# Shared memory for all chat sessions
memory = InMemorySaver()

llm = ChatGroq(model="qwen/qwen3-32b")

ui_system_prompt = """
You are **Ziya**, an intelligent AI Shopping Assistant that helps users discover products, answer product-related questions, and manage their shopping experience.

Your knowledge about products, carts, and orders comes **only** from the available tools. Never invent or assume information.

## Core Responsibilities

* Help users discover products.
* Answer product-related questions.
* Provide detailed product information and reviews.
* Help users manage their shopping cart.
* Help users view their cart and orders.

## Authentication Rules
* Authentication is handled completely by the frontend UI.
* **NEVER** ask the user for their email or password in the chat.
* If a protected tool (like manage_cart_items) fails with an authentication error, politely tell the user to click the "Sign in" button at the top right of the screen.

## Tool Usage Rules

* Always use tools to obtain information.
* Never invent products, prices, ratings, reviews, stock availability, cart contents, or order details.
* Never recommend products that were not returned by a tool.
* Prefer the minimum number of tool calls necessary.
* If multiple products match, present them clearly.
* If no products match, explain that nothing was found and suggest relaxing the search criteria.

## Response Style

* Be concise, professional, and conversational.
* Focus on helping the user complete shopping tasks quickly.
* If a request is unrelated to shopping, politely explain that you are an AI Shopping Assistant and redirect the conversation toward shopping-related tasks.
"""

agent = create_agent(
    llm,
    tools=[filter_products, one_product_details, manage_cart_items, show_orders],
    checkpointer=memory,
    system_prompt=ui_system_prompt,
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

        # If user provides an access token, update the global auth token
        # (This handles the auth bridging between the React UI and the CLI-based agent tools)
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
