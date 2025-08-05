import uuid
from sqlalchemy import UUID, Column, String
from app.infrastructure.database.init import Base

class User(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    role = Column(String, default="user")  # 'user' or 'admin'
