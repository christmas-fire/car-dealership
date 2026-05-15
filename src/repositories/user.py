from sqlalchemy import select
from sqlalchemy.orm import Session

from src.models.user import UserBase
from src.core.security import get_password_hash

class UserRepository():
    def __init__(self, db: Session) -> None:
        self.db = db

    def get_all(self) -> list[UserBase]:
        return self.db.scalars(select(UserBase)).all()

    def get_by_id(self, user_id: str) -> UserBase:
        return self.db.get(UserBase, user_id)

    def get_by_email(self, email: str) -> UserBase | None:
        query = select(UserBase).where(UserBase.email == email)

        result = self.db.execute(query)
        return result.scalar_one_or_none()

    def create(self, name: str, email: str, password: str, role: str) -> UserBase:
        new_user = UserBase(
            name=name,
            email=email,
            hashed_password=get_password_hash(password),
            role=role
        )
        self.db.add(new_user)
        return new_user

    def delete(self, user: UserBase):
        self.db.delete(user)
