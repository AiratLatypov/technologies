from domain.entities.user import User
from domain.repositories.user_repository import UserRepository


class RegisterUser:
    def __init__(self, user_repo: UserRepository):
        self.user_repo = user_repo

    def execute(self, pk: int, name: str, phone: str) -> User:
        user = User(id=pk, name=name, phone=phone)
        self.user_repo.save(user)
        return user
