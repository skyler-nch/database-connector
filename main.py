from fastapi import FastAPI
import uvicorn
from sqlalchemy import create_engine
from sqlalchemy import text
import os

from src.structs import MongoBody,MysqlBody

app = FastAPI()

@app.get("/")
async def root():
    return {"message":"Hello World","detail":"this is a database connection pool service"}

@app.post("/mysqldb")
async def mysql(body:MysqlBody):
    with mysqldb_engine.connect() as connection:
        results = connection.execute(text(body.query))
        connection.commit()
    output = {"status":1}
    if body.query[:6].upper() == "SELECT":
        output = (res for res in results.mappings())
    return output

@app.post("/mongodb")
async def mysql(body:MongoBody):
    return {"message":"this module is not done"}


if __name__ == "__main__":
    mysqldb_engine = create_engine(os.environ.get("MYSQL_CONN"))
    uvicorn.run(app)