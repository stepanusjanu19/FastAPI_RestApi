import uuid
from sqlalchemy import Column, String, Float, UUID
from app.infrastructure.database.init import Base

class Item(Base):
    __tablename__ = "items"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, index=True)
    description = Column(String, nullable=True)
    price = Column(Float)
    
    
