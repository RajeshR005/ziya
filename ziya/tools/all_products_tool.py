from langchain.tools import tool
import requests
from dotenv import load_dotenv
load_dotenv()
import os

BASE_API_URL=os.getenv("BASE_API_URL")

print(BASE_API_URL)

@tool
def all_products_details():

    response=requests.get(f"{BASE_API_URL}/get_all_products")

    return str(response.json())