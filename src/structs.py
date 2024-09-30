from pydantic import BaseModel

class MysqlBody(BaseModel):
    query: str

class MongoBody(BaseModel):
    database: str
    collection: str
    operation: str
    value: dict