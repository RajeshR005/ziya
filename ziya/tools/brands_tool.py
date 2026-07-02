from langchain.tools import tool
import requests
import os
from dotenv import load_dotenv

load_dotenv()

BASE_API_URL = os.getenv("BASE_API_URL")


@tool
def get_all_brands():
    """
    Retrieve all available product brands.

    Use this tool whenever the user specifies a brand, or when the brand
    is ambiguous or uncertain.

    Examples:
    - Samsung
    - Apple
    - Asus
    - Acer

    Always consult this tool before guessing brand names.
    """

    response = requests.get(f"{BASE_API_URL}/brands")

    response.raise_for_status()

    return response.json()