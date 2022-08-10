from lib2to3.pgen2.token import OP
from click import password_option
from pydantic import BaseModel 
from typing import Optional 

# user Model for user's registration. 
class UserValidator(BaseModel): 
    first_name      : str 
    last_name       : Optional[str] = None 
    email_address   : str 
    username        : str 
    password        : str
    phone_numer     : Optional[str] = None
    
