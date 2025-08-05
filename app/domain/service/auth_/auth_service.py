from passlib.context import CryptContext
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.users import User
from schema.users import UserCreate

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class AuthService:
    @staticmethod
    def hash_password(password: str):
        return pwd_context.hash(password)

    @staticmethod
    def verify_password(plain: str, hashed: str):
        return pwd_context.verify(plain, hashed)

    @staticmethod
    async def authenticate_user(db: AsyncSession, username: str, password: str):
        result = await db.execute(select(User).where(User.username == username))
        user = result.scalar_one_or_none()
        if user and AuthService.verify_password(password, user.hashed_password):
            return user
        return None

    @staticmethod
    async def register_user(db: AsyncSession, user_data: UserCreate):
        hashed = AuthService.hash_password(user_data.password)
        user = User(username=user_data.username, hashed_password=hashed, role=user_data.role)
        db.add(user)
        await db.commit()
        await db.refresh(user)
        return user
