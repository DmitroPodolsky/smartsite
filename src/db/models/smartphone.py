from datetime import datetime
from sqlalchemy import Column, DateTime, Integer, String, JSON, ForeignKey, Numeric
from sqlalchemy.orm import Relationship
from db.conection import Base

class Smartphone(Base):
    __tablename__ = "smartphones"
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), default=1, nullable=False)
    name = Column(String(200), nullable=False)
    brand = Column(String(50), nullable=False)
    price = Column(Numeric(10, 2), nullable=False)
    photo_urls = Column(JSON, nullable=False)
    cores_number = Column(Integer, nullable=False)
    build_in_memory = Column(Integer, nullable=False)
    ram = Column(Integer, nullable=False)
    diagonal = Column(Integer, nullable=False)
    refresh_rate = Column(Integer, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, onupdate=datetime.utcnow)
    
    user = Relationship("User", back_populates="smartphones")
    basket = Relationship("Basket", back_populates="smartphones", secondary="basket_smartphone_association")