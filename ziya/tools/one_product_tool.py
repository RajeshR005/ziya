from langchain.tools import tool
import requests


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
     
    response=requests.get(f"http://127.0.0.1:8000/ziya/get_one_product/{product_id}")
                        
    
    return str(response.json())
