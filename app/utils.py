import shutil
from pwdlib import PasswordHash
from dotenv import load_dotenv
import os
import sys
from datetime import datetime


password_hash=PasswordHash.recommended()


def hash_password(password:str):
    return password_hash.hash(password)

def verify_password(plain_password:str,hashed_password:str):
    return password_hash.verify(plain_password,hashed_password)

