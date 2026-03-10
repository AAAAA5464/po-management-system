# routers/vendors.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import Vendor
from schemas import VendorCreate, VendorResponse
from typing import List

router = APIRouter()

# GET all vendors
@router.get("/", response_model=List[VendorResponse])
def get_vendors(db: Session = Depends(get_db)):
    return db.query(Vendor).all()

# GET single vendor
@router.get("/{vendor_id}", response_model=VendorResponse)
def get_vendor(vendor_id: int, db: Session = Depends(get_db)):
    vendor = db.query(Vendor).filter(Vendor.id == vendor_id).first()
    if not vendor:
        raise HTTPException(status_code=404, detail="Vendor not found")
    return vendor

# POST create vendor
@router.post("/", response_model=VendorResponse)
def create_vendor(vendor: VendorCreate, db: Session = Depends(get_db)):
    try:
        new_vendor = Vendor(**vendor.model_dump())
        db.add(new_vendor)
        db.commit()
        db.refresh(new_vendor)
        return new_vendor
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=str(e))

# DELETE vendor
@router.delete("/{vendor_id}")
def delete_vendor(vendor_id: int, db: Session = Depends(get_db)):
    vendor = db.query(Vendor).filter(Vendor.id == vendor_id).first()
    if not vendor:
        raise HTTPException(status_code=404, detail="Vendor not found")
    db.delete(vendor)
    db.commit()
    return {"message": "Vendor deleted successfully"}