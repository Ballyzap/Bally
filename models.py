from pydantic import BaseModel
from typing import List
from uuid import UUID, uuid4
from typing import Optional
from enum import Enum


class Gender(str, Enum):
    Male = "Male"
    Female = "Female"

class Role(str, Enum):
    Admin = "Admin"
    User = "user"
    Student = "Student"
    Cleaner = "Cleaner"


class User(BaseModel):
    ID: Optional[UUID] = uuid4()
    First_Name: str
    Last_Name: str
    Middle_Name: Optional[str]
    Age: int
    Gender: Gender
    Roles: List[Role]
    Address: str
    Country: str


class UpdateUserRequest(BaseModel):
    First_Name: Optional[str]
    Last_Name: Optional[str]
    Middle_Name: Optional[str]
    Roles: Optional[List[Role]]