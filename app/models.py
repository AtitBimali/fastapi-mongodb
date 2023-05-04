from datetime import datetime
from typing import Optional
from bson import ObjectId
from pydantic import BaseModel,Field


class Task(BaseModel):
    id: Optional[str] = str(ObjectId())
    title: str
    description: Optional[str]
    completed: Optional[bool] = False
    created_at: Optional[datetime] = Field(default_factory=datetime.utcnow, alias="createdAt")
    updated_at: Optional[datetime] =Field(alias='updatedAt')

class User(BaseModel):
    id = Optional[str] = str(ObjectId())
    username = str(max_length=250, required=True)
    password = str(max_length=250, required=True)
    disabled = bool(default=False)
    date_created = datetime(default=datetime.utcnow)
    date_modified = datetime(default=datetime.utcnow)