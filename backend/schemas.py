# schemas.py
from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

# ── VENDOR SCHEMAS ─────────────────────────
class VendorCreate(BaseModel):
    name: str
    contact: str
    rating: Optional[float] = None

class VendorResponse(BaseModel):
    model_config = {"from_attributes": True}
    id: int
    name: str
    contact: str
    rating: Optional[float]
    created_at: datetime

# ── PRODUCT SCHEMAS ────────────────────────
class ProductCreate(BaseModel):
    name: str
    sku: str
    unit_price: float
    stock_level: int = 0
    category: Optional[str] = None

class ProductResponse(BaseModel):
    model_config = {"from_attributes": True}
    id: int
    name: str
    sku: str
    unit_price: float
    stock_level: int
    category: Optional[str]
    created_at: datetime

# ── PO ITEM SCHEMAS ────────────────────────
class POItemCreate(BaseModel):
    product_id: int
    quantity: int
    unit_price: float

class POItemResponse(BaseModel):
    model_config = {"from_attributes": True}
    id: int
    product_id: int
    quantity: int
    unit_price: float

# ── PURCHASE ORDER SCHEMAS ─────────────────
class PurchaseOrderCreate(BaseModel):
    vendor_id: int
    items: List[POItemCreate]

class PurchaseOrderResponse(BaseModel):
    model_config = {"from_attributes": True}
    id: int
    reference_no: str
    vendor_id: int
    total_amount: float
    status: str
    created_at: datetime
    po_items: List[POItemResponse] = []