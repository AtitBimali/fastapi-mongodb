from typing import Optional
from .models import Task,User
from datetime import datetime 
from pydantic import Field

# class TaskCreate(Task):
#     title: str
#     description: Optional[str]
#     completed: Optional[bool] = False
    
#     class Config:
#         allow_population_by_field_name = True

        

class TaskUpdate(Task):
    title: str
    description: Optional[str]
    completed: Optional[bool] = False
    updated_at: Optional[datetime] = Field(default_factory=datetime.utcnow, alias="updatedAt")

    class Config:
        allow_population_by_field_name = True


class NewUser(User):
    username: str
    password: str
crypt_context = CryptContext(schemes=["sha256_crypt", "md5_crypt"])

def get_password_hash(password):
    return crypt_context.hash(password)