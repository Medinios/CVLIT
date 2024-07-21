from sqlalchemy import UUID, Column, Date, String, func
import uuid
from app.db.base import Base


class User(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    createdAt = Column(Date, server_default=func.current_timestamp())
    updatedAt = Column(Date, server_default=func.current_timestamp(
    ), onupdate=func.current_timestamp())
    firstName = Column(String, nullable=False)
    lastName = Column(String, nullable=False)
    email = Column(String, nullable=False)
