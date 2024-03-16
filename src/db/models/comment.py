from datetime import datetime
from sqlalchemy import Column, DateTime, Integer, String, JSON, ForeignKey, Numeric
from sqlalchemy.orm import Relationship
from db.conection import Base

class Comment(Base):
    __tablename__ = "comments"
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    smartphone_id = Column(Integer, ForeignKey('smartphones.id'), nullable=False)
    message = Column(String(500), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, onupdate=datetime.utcnow)
    
    user = Relationship("User", back_populates="comments")
    smartphone = Relationship("Smartphone", back_populates="comments")