# main.py - App ka Starting Point

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import engine, Base
from routers import vendors, products, purchase_orders,ai

# FastAPI app banao
app = FastAPI(
    title="PO Management System",
    description="IV Innovations - Purchase Order Management",
    version="1.0.0"
)

# CORS - Frontend ko Backend se baat karne deta hai
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Database tables banao
Base.metadata.create_all(bind=engine)

# Routes register karo
app.include_router(vendors.router,        prefix="/api/vendors",  tags=["Vendors"])
app.include_router(products.router,       prefix="/api/products", tags=["Products"])
app.include_router(purchase_orders.router,prefix="/api/orders",   tags=["Orders"])
app.include_router(ai.router, prefix="/api/ai", tags=["AI"])
# Test route
@app.get("/")
def home():
    return {"message": "PO Management System API is running! 🚀"}