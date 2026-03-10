# routers/purchase_orders.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import PurchaseOrder, POItem, Product
from schemas import PurchaseOrderCreate, PurchaseOrderResponse
from typing import List
import datetime

router = APIRouter()

# ── CALCULATE TOTAL FUNCTION ───────────────
# PDF requirement: 5% tax automatically apply karo
def calculate_total(items, db: Session):
    subtotal = 0
    for item in items:
        subtotal += item.quantity * item.unit_price
    tax = subtotal * 0.05        # 5% tax
    total = subtotal + tax
    return round(total, 2)

# ── GENERATE REFERENCE NUMBER ──────────────
def generate_reference():
    now = datetime.datetime.now()
    return f"PO-{now.year}-{now.strftime('%m%d%H%M%S')}"

# GET all purchase orders
@router.get("/", response_model=List[PurchaseOrderResponse])
def get_orders(db: Session = Depends(get_db)):
    return db.query(PurchaseOrder).all()

# GET single purchase order
@router.get("/{order_id}", response_model=PurchaseOrderResponse)
def get_order(order_id: int, db: Session = Depends(get_db)):
    order = db.query(PurchaseOrder).filter(PurchaseOrder.id == order_id).first()
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return order

# POST create purchase order
@router.post("/", response_model=PurchaseOrderResponse)
def create_order(order: PurchaseOrderCreate, db: Session = Depends(get_db)):
    try:
        # Step 1: Calculate total with 5% tax
        total = calculate_total(order.items, db)

        # Step 2: Create the Purchase Order
        new_order = PurchaseOrder(
            reference_no = generate_reference(),
            vendor_id    = order.vendor_id,
            total_amount = total,
            status       = "Draft"
        )
        db.add(new_order)
        db.flush()  # ID milti hai bina commit ke

        # Step 3: Add each item to po_items table
        for item in order.items:
            po_item = POItem(
                po_id      = new_order.id,
                product_id = item.product_id,
                quantity   = item.quantity,
                unit_price = item.unit_price
            )
            db.add(po_item)

        db.commit()
        db.refresh(new_order)
        return new_order

    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=str(e))

# PUT update order status
@router.put("/{order_id}/status")
def update_status(order_id: int, status: str, db: Session = Depends(get_db)):
    order = db.query(PurchaseOrder).filter(PurchaseOrder.id == order_id).first()
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    
    allowed = ["Draft", "Confirmed", "Received", "Cancelled"]
    if status not in allowed:
        raise HTTPException(status_code=400, detail=f"Status must be one of {allowed}")
    
    order.status = status
    db.commit()
    return {"message": f"Status updated to {status}"}

# DELETE order
@router.delete("/{order_id}")
def delete_order(order_id: int, db: Session = Depends(get_db)):
    order = db.query(PurchaseOrder).filter(PurchaseOrder.id == order_id).first()
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    db.delete(order)
    db.commit()
    return {"message": "Order deleted successfully"}