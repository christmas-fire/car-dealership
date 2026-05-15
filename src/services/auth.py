from fastapi import APIRouter, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from src.core.exeptions import UserAlreadyExists, InvalidCreds
from src.core.security import verify_password, create_access_token, get_password_hash
from src.repositories.user import UserRepository
from src.schemas.auth import LoginResponse, LoginRequest
from src.schemas.user import UserCreateSchema, UserSchema

router = APIRouter(prefix="/auth", tags=["Auth"])

class AuthService():
    def __init__(self, db: Session) -> None:
        self.db = db
        self.user_repository = UserRepository(db)

    def register(self, user: UserCreateSchema) -> UserSchema:
        user_exists = self.user_repository.get_by_email(user.email)
        if user_exists:
            raise UserAlreadyExists(message=f"User with same email already exists")

        users_orm = self.user_repository.create(
            name=user.name,
            email=user.email,
            password=user.password,
            role=user.role
        )
        self.db.commit()

        return UserSchema.model_validate(users_orm)

    def login(self, creds: OAuth2PasswordRequestForm) -> LoginResponse:
        user = self.user_repository.get_by_email(email=creds.username)
        if not user or not verify_password(creds.password, user.hashed_password):
            raise InvalidCreds(message="Incorrect email or password")

        access_token = create_access_token(data={"sub": user.email})
        return LoginResponse(access_token=access_token, token_type="bearer")
