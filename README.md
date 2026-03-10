# PO Management System

A full-stack **Purchase Order Management System** built using **FastAPI, PostgreSQL and a simple frontend dashboard**.
The system allows businesses to manage vendors, products and purchase orders efficiently.

It also includes an **AI feature using Gemini API** to automatically generate product descriptions.

---

# Project Overview

This project demonstrates how to build a **modern REST API with FastAPI** and integrate it with a database and frontend interface.
It follows a modular backend architecture and shows how AI services can be integrated into business applications.

The system supports:

* Vendor management
* Product management
* Purchase order creation
* Dynamic product rows
* AI-generated product descriptions

---

# Features

* Vendor CRUD operations
* Product CRUD operations
* Purchase Order creation with multiple products
* Dynamic order rows in frontend dashboard
* AI generated product description using Gemini API
* RESTful API architecture
* PostgreSQL database integration
* FastAPI automatic API documentation

---

# Tech Stack

**Backend**

* FastAPI
* Python
* SQLAlchemy
* PostgreSQL

**Frontend**

* HTML
* JavaScript
* Fetch API

**AI Integration**

* Google Gemini API

**Tools**

* Git
* GitHub
* VS Code
* pgAdmin

---

# Project Structure

```
po-management-system
│
├ backend
│   ├ routers
│   │   ├ vendors.py
│   │   ├ products.py
│   │   ├ purchase_orders.py
│   │   └ ai.py
│   │
│   ├ database.py
│   ├ models.py
│   ├ schemas.py
│   └ main.py
│
├ frontend
│   └ index.html
│
├ screenshots
├ requirements.txt
├ .env.example
└ README.md
```

---

# Setup Instructions

## 1 Clone Repository

```
git clone https://github.com/AAAAA5464/po-management-system.git
cd po-management-system
```

---

## 2 Create Virtual Environment

```
python -m venv venv
venv\Scripts\activate
```

---

## 3 Install Dependencies

```
pip install -r requirements.txt
```

---

## 4 Create Environment File

Copy example file:

```
copy .env.example .env
```

Add your database credentials and Gemini API key.

---

## 5 Run Backend Server

```
cd backend
uvicorn main:app --reload
```

Open API documentation:

```
http://127.0.0.1:8000/docs
```

---

## 6 Run Frontend

Open:

```
frontend/index.html
```

You can also run it using the **Live Server extension in VS Code**.

---

# API Endpoints

## Vendors

```
GET    /api/vendors
POST   /api/vendors
GET    /api/vendors/{vendor_id}
DELETE /api/vendors/{vendor_id}
```

## Products

```
GET    /api/products
POST   /api/products
GET    /api/products/{product_id}
```

## Purchase Orders

```
POST /api/orders
GET  /api/orders
```

---

# Screenshots

## API Documentation

Swagger UI provided by FastAPI:

![API Docs](screenshots/api.png)

---

## Dashboard

Frontend interface for managing purchase orders.

![Dashboard](screenshots/dashboard.png)

---

## Database

PostgreSQL database tables viewed in pgAdmin.

![Database](screenshots/database.png)

---

# Future Improvements

* User authentication using JWT
* Role-based access control
* Advanced analytics dashboard
* Docker containerization
* Deployment to cloud

---

# Author

Anuj Rawat
B.Tech Computer Science
Data Analyst / AI Enthusiast

GitHub:
https://github.com/AAAAA5464
