from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .base import Base
from .order_product_assotiation import order_product_association  # ← ИМПОРТИРУЙ ТАБЛИЦУ

class Order(Base):
    __tablename__ = "orders"
    
    id = Column(Integer, primary_key=True)
    promocode = Column(String, nullable=True)
    
    # Отношение через таблицу
    products = relationship(
        "Product",
        secondary=order_product_association,  # ← ПЕРЕДАВАЙ ТАБЛИЦУ, а не класс
        back_populates="orders"
    )
