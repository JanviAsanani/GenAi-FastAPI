from fastapi import APIRouter
from models import User

router = APIRouter()

@router.post("/", response_model=User, summary="Create a new user")
async def create_user(user: User):
    return user