from langchain.tools import tool
import requests
import os
from dotenv import load_dotenv

load_dotenv()

BASE_API_URL = os.getenv("BASE_API_URL")


@tool
def get_all_categories():
    """
    Retrieve all available product categories.

    Use this tool whenever the user's requested category is unclear,
    ambiguous, or may not exactly match the categories stored in the catalog.

    Examples:
    - laptops
    - gaming laptops
    - mobiles
    - televisions

    Always consult this tool before guessing category names.
    """

    response = requests.get(f"{BASE_API_URL}/categories")

    response.raise_for_status()

    return response.json()