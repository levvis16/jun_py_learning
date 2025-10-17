from sqlalchemy import Table, Column, ForeignKey, Integer, UniqueConstraint
from .base import Base

# ТОЛЬКО таблица, без класса
order_product_association = Table(
    "order_product_association",
    Base.metadata,
    Column("id", Integer, primary_key=True),
    Column("order_id", ForeignKey("orders.id"), nullable=False),
    Column("product_id", ForeignKey("products.id"), nullable=False),
    UniqueConstraint("order_id", "product_id", name="idx_unique_order_product"),
)