from langchain.tools import tool
import requests
from ziya.tools.auth_tool import auth_headers
from dotenv import load_dotenv
load_dotenv()
import os

BASE_API_URL=os.getenv("BASE_API_URL")
@tool
def show_orders():
    """
    Retrieve the current user's order or cart summary.

    Use this tool when the user wants to:
    - View their cart
    - Check their current orders
    - See items they have added to purchase
    - Verify order/cart contents

    Returns:
    - List of items in the user's cart/order
    - Product details for each item
    - Quantity information
    - Any available pricing summary

    Important:
    - Do not assume or modify data.
    - Always display exactly what the tool returns.
    """
    response=requests.get(f"{BASE_API_URL}/get_cart",headers=auth_headers())

    return str(response.json())