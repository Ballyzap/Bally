from fastapi import FastAPI, Path
from fastapi import HTTPException
from models import User, Gender, Role
from typing import List
from uuid import UUID, uuid4
from typing import Optional
from models import UpdateUserRequest

app = FastAPI()

DB: List[User] = [
    User(
        ID=UUID("808f6c1c-6893-4925-86e3-c9f17d64ecf7"),
        First_Name="Sasha",
        Last_Name="Obama",
        Middle_Name="",
        Age= 25,
        Gender=Gender.Female,
        Roles=[Role.User, Role.Student],
        Address="Chicago",
        Country="America"
    ),
    User(
        ID=UUID("08613aed-0fc6-463a-9549-4fa8a16664af"),
        First_Name="Frank",
        Last_Name="Zack",
        Middle_Name="Johnson",
        Age= 18,
        Gender=Gender.Male,
        Roles=[Role.Admin],
        Address="Lisbon",
        Country="Portugal"
    ),
    User(
        ID=UUID("dfdbe61d-0e0c-4640-9d1c-dabb54d98ddb"),
        First_Name="Sophie",
        Last_Name="Mosh",
        Middle_Name="",
        Age= 21,
        Gender=Gender.Female,
        Roles=[Role.Cleaner, Role.User],
        Address="Lagos",
        Country="Nigeria"
    )
]


@app.get("/m1/users")
async def get_users():
    return DB;


@app.post("/m1/users")
async def register_user(data: User):
    DB.append(data)
    return{"ID": data.ID}


@app.put("/m1/users/{user_id}")
async def update_user(*, user_id: Optional[UUID] = Path(description="Input user ID"), data: UpdateUserRequest):
    for love in DB:
        if love.ID == user_id:
            if data.First_Name is not None:
                love.First_Name = data.First_Name
            if data.Last_Name is not None:
                love.Last_Name = data.Last_Name
            if data.Middle_Name is not None:
                love.Middle_Name = data.Middle_Name
            if data.Roles is not None:
                love.Roles = data.Roles
                return{"Message": "User updated successfully"}
    raise HTTPException(
        status_code=404,
        detail=f"User with ID: {user_id} does not exists"
    )


@app.delete("/m1/users/{user_id}")
async def delete_user(*, user_id: Optional[UUID] = Path(description="Input user ID")):
    for data in DB:
        if data.ID == user_id:
            DB.remove(data)
            return{"Message": "User deleted successfully"}
    raise HTTPException(
        status_code=404,
        detail=f"User with ID: {user_id} does not exist"
    )
