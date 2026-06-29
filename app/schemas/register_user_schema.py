from typing import Optional
from pydantic import BaseModel,EmailStr
from datetime import date

class reg_user(BaseModel):
    first_name:str
    last_name:str
    date_of_birth:date
    email:EmailStr
    password:str
    confirm_password:str
    phone_number:str
    