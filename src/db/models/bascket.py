from datetime import datetime
from sqlalchemy import Column, DateTime, Integer, String, JSON, ForeignKey, Numeric
from sqlalchemy.orm import Relationship
from db.conection import Base

class Bascet(Base):
    __tablename__ = "bascet"
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    smartphone_id = Column(Integer, ForeignKey('smartphones.id'), nullable=False)
    smartphones = Column(JSON, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, onupdate=datetime.utcnow)
    
    user = Relationship("User", back_populates="bascet")
    smartphone = Relationship("Smartphone", back_populates="bascet")
    