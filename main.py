from fastapi import FastAPI  
from models import BlogEntry  

app=FastAPI()  

@app.get("/")
async def get_root():  
    return {"message":"Hello World"} 

@app.post("/new_post") 
async def create_post(entry:BlogEntry):
    return {"post":entry}