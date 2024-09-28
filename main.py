from fastapi import FastAPI

from src.structs import MongoBody,MysqlBody

app = FastAPI()

@app.get("/")
async def root():
    return {"message":"Hello World","detail":"this is a database connection pool service"}

@app.post("/mysqldb")
async def mysql(body:MysqlBody):
    # i need to know the database, query

    return body

@app.post("/mongodb")
async def mysql(body:MongoBody):
    #i need to know the operation, value, database, collection
    return body
    