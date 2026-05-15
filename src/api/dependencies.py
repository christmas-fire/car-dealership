import jwt
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from src.core.config import get_settings
from src.repositories.user import UserRepository
from src.schemas.user import UserSchema
from src.db.session import get_db
from src.services.brand import BrandService
from src.services.model import ModelService
from src.services.car import CarService
from src.services.user import UserService
from src.services.auth import AuthService

def get_brand_service(db: Session = Depends(get_db)):
    """DI BrandService"""
    return BrandService(db)


def get_model_service(db: Session = Depends(get_db)):
    """DI ModelService"""
    return ModelService(db)


def get_car_service(db: Session = Depends(get_db)):
    """DI CarService"""
    return CarService(db)


def get_user_service(db: Session = Depends(get_db)):
    """DI UserService"""
    return UserService(db)


def get_auth_service(db: Session = Depends(get_db)):
    """DI AuthService"""
    return AuthService(db)


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

async def get_current_user(
        token: str = Depends(oauth2_scheme),
        db: Session = Depends(get_db)
) -> UserSchema:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        settings = get_settings()
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
    except jwt.InvalidTokenError:
        raise credentials_exception

    user_repo = UserRepository(db)
    user = user_repo.get_by_email(email=email)
    if user is None:
        raise credentials_exception
    return UserSchema.model_validate(user)
