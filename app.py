from fastapi import FastAPI
from typing import Optional 
from pydantic import BaseModel
import users.users as users 


class Item(BaseModel): 
    name: str 
    description: Optional[str] = None 
    price: float 
    tax: Optional[float] = None

app = FastAPI()

## test connection

@app.get("/test")
async def test_connection(): 
    return {
        "message": "test SuccessFull"
    }

@app.get("/item/{item_id}")
async def get_item(item_id : int): 
    return {
        "message": "Item Id",
        "item_id": item_id
    }


@app.post("/get_item")
async def get_item_data(item: Item): 
    return item 


app.include_router(users.router)
