# models.py
# Har class = ek database table

from sqlalchemy import Column, Integer, String, Numeric, ForeignKey, TIMESTAMP
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy.sql import func

Base = declarative_base()

# ── VENDORS TABLE ──────────────────────────
class Vendor(Base):
    __tablename__ = "vendors"

    id         = Column(Integer, primary_key=True, index=True)
    name       = Column(String(100), nullable=False)
    contact    = Column(String(100), nullable=False)
    rating     = Column(Numeric(2, 1))
    created_at = Column(TIMESTAMP, server_default=func.now())

    purchase_orders = relationship("PurchaseOrder", back_populates="vendor")


# ── PRODUCTS TABLE ─────────────────────────
class Product(Base):
    __tablename__ = "products"

    id          = Column(Integer, primary_key=True, index=True)
    name        = Column(String(100), nullable=False)
    sku         = Column(String(50), unique=True, nullable=False)
    unit_price  = Column(Numeric(10, 2), nullable=False)
    stock_level = Column(Integer, default=0)
    category    = Column(String(50))
    created_at  = Column(TIMESTAMP, server_default=func.now())

    po_items = relationship("POItem", back_populates="product")


# ── PURCHASE ORDERS TABLE ──────────────────
class PurchaseOrder(Base):
    __tablename__ = "purchase_orders"

    id           = Column(Integer, primary_key=True, index=True)
    reference_no = Column(String(50), unique=True, nullable=False)
    vendor_id    = Column(Integer, ForeignKey("vendors.id"), nullable=False)
    total_amount = Column(Numeric(10, 2), default=0)
    status       = Column(String(20), default="Draft")
    created_at   = Column(TIMESTAMP, server_default=func.now())

    vendor   = relationship("Vendor", back_populates="purchase_orders")
    po_items = relationship("POItem", back_populates="purchase_order")


# ── PO ITEMS TABLE ─────────────────────────
class POItem(Base):
    __tablename__ = "po_items"

    id         = Column(Integer, primary_key=True, index=True)
    po_id      = Column(Integer, ForeignKey("purchase_orders.id"), nullable=False)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)
    quantity   = Column(Integer, nullable=False)
    unit_price = Column(Numeric(10, 2), nullable=False)

    purchase_order = relationship("PurchaseOrder", back_populates="po_items")
    product        = relationship("Product", back_populates="po_items")