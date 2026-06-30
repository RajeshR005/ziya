from langchain.tools import tool
import requests
from dotenv import load_dotenv
load_dotenv()
import os

BASE_API_URL=os.getenv("BASE_API_URL")

@tool
def filter_products(
    brand: str = None,
    category: str = None,
    min_price: float = None,
    max_price: float = None,
    min_rating: float = None,
    max_rating: float = None,
):
    """
    Search the product catalog using one or more filters.

    Use this tool whenever the user wants to browse or discover products.

    Supported filters:
    - brand
    - category
    - minimum price
    - maximum price
    - minimum rating
    - maximum rating

    Examples:
    - Samsung phones under ₹30,000
    - Apple laptops
    - Earbuds above 4.5 rating
    - Smartphones between ₹20,000 and ₹40,000

    Returns matching products with:
    - Product name
    - Brand
    - Category
    - Description
    - Price
    - Stock availability
    - Average rating
    """

    response = requests.get(
        f"{BASE_API_URL}/filter_products/",
        params={
            "brand":brand,
            "category":category,
            "min_price":min_price,
            "max_price":max_price,
            "min_rating":min_rating,
            "max_rating":max_rating       }
    )

    return str(response.json())
