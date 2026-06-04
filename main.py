from fastapi import FastAPI , HTTPException

from pydantic import ValidationError
from models import BlogEntry  

app=FastAPI()  

@app.get("/")
async def get_root():  
    return {"message":"Hello World"} 

@app.post("/new_post") 
async def create_post(data:dict): 
    try:
        entry=BlogEntry.model_validate(data)
        return {"message":"Post Has been created successfully"}
    except ValidationError as e:  
        raise HTTPException(
            status_code=400,  
            detail=f"model is missing the following data: {e.errors()}"
        )

    