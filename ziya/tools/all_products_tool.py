from langchain.tools import tool
import requests



@tool
def all_products_details():

    response=requests.get("http://127.0.0.1:8000/ziya/get_all_products")

    return str(response.json())