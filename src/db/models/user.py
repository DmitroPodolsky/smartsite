from datetime import datetime
from sqlalchemy import Boolean, Column, DateTime, Integer, String
from werkzeug.security import generate_password_hash, check_password_hash
from db.conection import Base


class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True)
    surname = Column(String(50))
    email = Column(String(120), unique=True)
    password_hash = Column("password", String(120), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, onupdate=datetime.utcnow)
    isverified = Column(Boolean, default=False, nullable=False)
    isadmin = Column(Boolean, default=False, nullable=False)

    @property
    def password(self):
        raise AttributeError('password: write-only field')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)