from sqlalchemy.orm import Session

from src.repositories.user import UserRepository
from src.schemas.user import UserSchema, UserCreateSchema, UserUpdateSchema
from src.core.exeptions import BrandNotFound

class UserService():
    def __init__(self, db: Session) -> None:
        self.db = db
        self.user_repository = UserRepository(db)

    def list_users(self) -> list[UserSchema]:
        users_orm = self.user_repository.get_all()
        return [UserSchema.model_validate(user) for user in users_orm]

    def create_user(self, user: UserCreateSchema) -> UserSchema:
        user_orm = self.user_repository.create(
            name=user.name,
            email=user.email,
            password=user.password,
        )
        self.db.commit()
        return UserSchema.model_validate(user_orm)

    def delete_user(self, user_id: str) -> None:
        user_for_delete = self.user_repository.get_by_id(user_id=user_id)
        if not user_for_delete:
            raise BrandNotFound(f"User with id={user_id} not found")

        self.user_repository.delete(user_for_delete)
        self.db.commit()
