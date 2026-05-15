from fastapi import APIRouter, Depends

from src.api.dependencies import get_user_service
from src.schemas.user import UserSchema
from src.services.user import UserService

router = APIRouter(prefix="/users", tags=["users"])

@router.get("/")
def read_users(
    user_service: UserService = Depends(get_user_service)
) -> list[UserSchema]:
    return user_service.list_users()
