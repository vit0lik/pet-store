from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from ..database import Base


class Supplier(Base):
    __tablename__ = "suppliers"
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(200), nullable=False)
    contact_person = Column(String(100))
    email = Column(String(255))
    phone = Column(String(15))
    address = Column(String(255))
    
    products = relationship("Product", back_populates="supplier")