from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel


class User(BaseModel):
    email: str
    name: Optional[str] = None
    age: int
    mobile_number: Optional[int] = None


app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World!"}


@app.post("/users/")
async def create_user(user: User):
    return user


@app.get("/users/{user_id}")
async def user_details(user_id: int, q: str | None = None, short: bool = False):
    user = {"user_id": user_id}
    if q:
        user.update({
            "q": q
        })
    if short:
        user.update({
            "description": "This is an amazing user that has a long description"
        })
    return user
