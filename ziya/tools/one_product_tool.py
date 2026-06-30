from langchain.tools import tool
import requests
from dotenv import load_dotenv
load_dotenv()
import os

BASE_API_URL=os.getenv("BASE_API_URL")

@tool
def one_product_details(product_id: int):
    """
    Retrieve complete information for a single product.

    Use this tool when the user asks for details about a specific product or wants
    to know its reviews, description, specifications, stock availability, or rating.

    Requires:
    - product_id

    Returns:
    - Product details
    - Price
    - Stock status
    - Average rating
    - Customer reviews
"""
     
    response=requests.get(f"{BASE_API_URL}/get_one_product/{product_id}")
                        
    
    return str(response.json())
