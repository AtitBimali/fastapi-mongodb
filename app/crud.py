from pymongo import MongoClient
from bson.objectid import ObjectId
from typing import List
from schemas import TaskCreate, TaskUpdate, Task

client = MongoClient("<MONGODB_CONNECTION_STRING>")
db = client["todo"]
collection = db["tasks"]

def create_task(task: TaskCreate) -> Task:
    result = collection.insert_one(task.dict())
    task_id = str(result.inserted_id)
    task = Task(**task.dict(), id=task_id)
    return task

def read_task(task_id: str) -> Task:
    task = collection.find_one({"_id": ObjectId(task_id)})
    return Task(**task, id=task_id)

def read_tasks() -> List[Task]:
    tasks = []
    for task in collection.find():
        task_id = str(task["_id"])
        tasks.append(Task(**task, id=task_id))
    return tasks

def update_task(task_id: str, task: TaskUpdate) -> Task:
    task_data = task.dict(exclude_unset=True)
    collection.update_one({"_id": ObjectId(task_id)}, {"$set": task_data})
    return read_task(task_id)

def delete_task(task_id: str) -> None:
    collection.delete_one({"_id": ObjectId(task_id)})
