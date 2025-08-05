from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from infrastructure.utils.init import verify_token
from domain.models.users import User
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from infrastructure.database.init import get_db

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/users/login")

async def get_current_user(token: str = Depends(oauth2_scheme), db: AsyncSession = Depends(get_db)) -> User:
    payload = verify_token(token)
    if not payload:
        raise HTTPException(status_code=401, detail="Invalid token")
    result = await db.execute(select(User).where(User.username == payload["sub"]))
    user = result.scalar_one_or_none()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

def require_role(role: str):
    async def role_checker(user: User = Depends(get_current_user)):
        if user.role != role:
            raise HTTPException(status_code=403, detail="Forbidden")
        return user
    return role_checker
