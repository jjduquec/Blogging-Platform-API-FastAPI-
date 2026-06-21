from pydantic import BaseModel


class BlogEntry(BaseModel): 
    id:optional[int]=None
    title:str  
    content:str  
    category:str  
    tags:list  
#https://medium.com/@parth.khajgiwale/building-a-crud-api-with-fastapi-mysql-and-postman-8e849e62d9fe