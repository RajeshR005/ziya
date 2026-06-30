import requests
from langchain.tools import tool
from dotenv import load_dotenv
load_dotenv()
import os

BASE_API_URL=os.getenv("BASE_API_URL")
BASE_URL = BASE_API_URL

ACCESS_TOKEN = None

@tool
def login(username: str, password: str):
    """
Authenticate a registered user and start an authenticated shopping session.

Use this tool only when authentication is required for protected operations.

Protected operations include:

* Adding products to the cart
* Updating cart quantities
* Removing cart items
* Viewing the shopping cart
* Viewing orders

Required inputs:

* username: Registered email address
* password: User password

On successful authentication:

* A JWT access token is securely stored for the current conversation session.
* All subsequent authenticated tool calls automatically use the stored token.
* The user does not need to log in again during the current session unless the token expires.

Do not use this tool for product discovery or viewing product details.
"""

    global ACCESS_TOKEN

    response = requests.post(
        f"{BASE_URL}/login",
        data={
            "username": username,
            "password": password,
        },
    )

    response.raise_for_status()

    ACCESS_TOKEN = response.json()["access_token"]

    return {"ACCESS_TOKEN":ACCESS_TOKEN,"msg":"Use this Access token for the Auth_Headers"}


def auth_headers():
    return {
        "Authorization": f"Bearer {ACCESS_TOKEN}"
    }