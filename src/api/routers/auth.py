from fastapi import APIRouter, status, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm

from loguru import logger

from src.core.exeptions import UserAlreadyExists, InvalidCreds
from src.schemas.auth import LoginResponse
from src.schemas.user import UserCreateSchema, UserSchema
from src.services.auth import AuthService
from src.api.dependencies import get_auth_service

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/register", status_code=status.HTTP_201_CREATED)
def register(
        user: UserCreateSchema,
        auth_service: AuthService = Depends(get_auth_service),
) -> UserSchema:
    try:
        return auth_service.register(user=user)
    except UserAlreadyExists as e:
        logger.exception(e.message)
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=e.message)


@router.post("/login")
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    auth_service: AuthService = Depends(get_auth_service)
) -> LoginResponse:
    try:
        return auth_service.login(creds=form_data)
    except InvalidCreds as e:
        logger.exception(e.message)
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=e.message)
