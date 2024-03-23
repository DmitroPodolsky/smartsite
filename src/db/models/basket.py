from datetime import datetime
from sqlalchemy import Column, DateTime, Integer, JSON, ForeignKey
from sqlalchemy.orm import Relationship
from db.conection import Base

class Bascet(Base):
    __tablename__ = "baskets"
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    smartphone_id = Column(Integer, ForeignKey('smartphones.id'), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, onupdate=datetime.utcnow)
    
    user = Relationship("User", back_populates="baskets", uselist=False)
    smartphone = Relationship("Smartphone", back_populates="baskets", secondary="basket_smartphone_association")