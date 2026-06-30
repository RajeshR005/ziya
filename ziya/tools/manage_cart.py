from langchain.tools import tool
import requests
from ziya.tools.auth_tool import auth_headers
from dotenv import load_dotenv
load_dotenv()
import os

BASE_API_URL=os.getenv("BASE_API_URL")

@tool
def manage_cart_items(action:str,product_id:int=None,quantity:int=None,cart_item_id:int=None):
   """
    Manage the user's shopping cart.

    Actions:

    - add
        Add a product to the cart.
        Requires:
        - product_id
        - quantity

    - update
        Update the quantity of an existing cart item.
        Requires:
        - cart_item_id
        - quantity

    Setting quantity to 0 removes the item from the cart.

    Use this tool whenever the user wants to:
    - Add products
    - Change quantities
    - Remove products
   """
   if action=="add":
        response=requests.post(f"{BASE_API_URL}/cart",params={
            "product_id":product_id,
            "quantity":quantity

        },headers=auth_headers())
        return str(response.json())
        
   elif action == "update":
        response=requests.post(f"{BASE_API_URL}/cart_update",
                              params={
                                  "cart_item_id":cart_item_id,
                                  "quantity":quantity
                                  
                              },headers=auth_headers())
        return str(response.json())


