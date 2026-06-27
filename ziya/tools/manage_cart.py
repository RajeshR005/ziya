from langchain.tools import tool
import requests

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
        response=requests.post("http://127.0.0.1:8000/ziya/cart",params={
            "product_id":product_id,
            "user_id":1,
            "quantity":quantity

        })
        return str(response.json())
        
   elif action == "update":
        response=requests.post("http://127.0.0.1:8000/ziya/cart_update",
                              params={
                                  "cart_item_id":cart_item_id,
                                  "user_id":1,
                                  "quantity":quantity
                                  
                              })
        return str(response.json())


