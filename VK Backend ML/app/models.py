from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, BigInteger, Boolean, DateTime
from datetime import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    user_id = Column(BigInteger, primary_key=True, index=True)
    greeted = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)
