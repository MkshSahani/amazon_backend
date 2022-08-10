from fastapi import APIRouter
from .user_validator import UserValidator
from response import responses
import logging
import database_service.services as db_service 

logger = logging.Logger(__name__)

router = APIRouter(
    prefix="/user",
    tags=["user"]
)


@router.get("/get_user_list")
async def get_user_list():
    return {
        "working": "successFull"
    }

@router.post("/register_user")
async def register_user(user_details: UserValidator): 
    try:
        user_details = user_details.dict() # user details
        result = db_service.execute_query(sql_query="SELECT * FROM test_table")
        print(result)
        return responses.SUCCESS_FULL
    except Exception as e:
        print(e)
        return responses.SHOW_ERROR_OCCURED

    
