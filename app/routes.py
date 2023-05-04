from fastapi import APIRouter, Body, Request, HTTPException
from .models import Task
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from typing import List
from .config import settings
from pymongo import mongo_client
from .schemas import TaskUpdate

router = APIRouter()
client = mongo_client.MongoClient(settings.MONGODB_URL)
database = client[settings.MONGODB_NAME]
collection = database["Task"]

@router.get('/', response_description="List all Tasks",response_model=List[Task])
async def list_tasks(request: Request):
    Tasks = list(collection.find())
    return Tasks


@router.post('/', response_description="Create a Task")
async def create_task(request: Request, task: Task = Body(...)):
    task = jsonable_encoder(task)
    existing_task = collection.find_one({"title": task["title"]})
    # if existing_task:
    #     return JSONResponse(content={"detail": "Task with the same title already exists."}, status_code=422)
    new_task = collection.insert_one(task)
    created_task = collection.find_one({"_id": new_task.inserted_id})
    created_task["_id"] = str(created_task["_id"])  # Convert ObjectId to string
    return JSONResponse(content=created_task, status_code=200)

@router.put('/{task_id}', response_description="Update a Task")
async def update_task(request: Request, task_id: str, task: TaskUpdate = Body(...)):
    # Check if task exists
    if not collection.find_one({"id": task_id}):
        raise HTTPException(status_code=404, detail="Task not found")
    # Update task
    updated_task = jsonable_encoder(task)
    collection.update_one({"id": str(task_id)}, {"$set": updated_task})
    return {"message": "Task updated successfully"}

@router.delete('/{task_id}', response_description="Delete a Task")
async def delete_task(request: Request, task_id: str):
    # Check if task exists
    if not collection.find_one({"id": str(task_id)}):
        raise HTTPException(status_code=404, detail="Task not found")
    # Delete task
    collection.delete_one({"id": str(task_id)})
    return {"message": "Task deleted successfully"}
