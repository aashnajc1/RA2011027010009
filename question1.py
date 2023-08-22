from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name : str
    price : float
    brand : Optional[str] = None

class UpdateItem(BaseModel):
    name : Optional[str] = None
    price : Optional[float] = None
    brand : Optional[str] = None

invetory = {}

#path parameters
@app.get("/get-item/{item_id}")
def get_item(item_id:int = Path(description= "Enter the ID", gt = 0, lt = 2)):
    return invetory[item_id]
#query parameters
@app.get("/get-by-name")
def get_item(*, item_id:int, name:Optional[str] = None,test : int):
    for item_id in invetory:
        if invetory[item_id].name == name:
            return invetory[item_id]
    return {"Data" : "Not found"}

#creating item through a method
@app.post("/create-item/{item_id}")
def create_item(item_id:int, item:Item):
    if item_id in invetory:
        return {"Error" : "Item ID already exists"}

    invetory[item_id] = item
    return invetory[item_id]

#update item
@app.put("/update-item/{item_id}")
def update_item(item_id : int, item : UpdateItem):
    if item_id not in inventory:
        return {"Error" : "Item ID does not exist"}
    if item.name != None:
        inventory[item_id].name = item.name
    if item.price != None:
        inventory[item_id].price = item.price
    if item.brand != None:
        inventory[item_id].brand = item.brand
    return invetory[item_id]

#delete item
@app.delete("/delete-item")
def delete_item(item_id:int = Query(..., description = "Enter the ID")):
    if item_id not in inventory:
       return {"Error" : "ID doesnt exist"}
    del invetory[item_id]
    return {"Success" : "Item deleted"}
