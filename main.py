from fastapi import FastAPI
from dotenv import dotenv_values
# from pymongo import MongoClient
from app.routes import router
from pymongo import mongo_client

config = dotenv_values(".env")

app = FastAPI()

# @app.get("/")
# async def root():
#     return {"message": "API using Fast API and pymongo"}

@app.on_event("startup")
def startup_db_client():
    
    app.mongodb_client = mongo_client.MongoClient(config["DB_URL"])
    app.database = app.mongodb_client[config["DB_NAME"]]
    print("Connected to the MongoDB database!")

@app.on_event("shutdown")
def shutdown_db_client():
    app.mongodb_client.close()

app.include_router(router, tags=["list"], prefix="")