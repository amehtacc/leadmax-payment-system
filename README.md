# LeadMax Payment System API

A backend payment system built using Django REST Framework and PostgreSQL.  
This project demonstrates API design, authentication, banking operations, payment transactions, and business logic implementation.

---

# Features

## User APIs
- Create User
- Update User
- Delete User
- Get User Profile
- Get Users List

## Authentication APIs
- JWT Authentication
- Login User
- Refresh Access Token

## Bank Account APIs
- Add Bank Account
- Get User Bank Accounts
- Delete Bank Account
- Top-up Bank Account Balance
- Maximum 3 bank accounts per user

## Payment APIs
- Transfer Money Between Accounts
- Transaction History
- SUCCESS and FAILED transaction tracking
- Insufficient balance handling
- Atomic payment transactions

---

# Tech Stack

- Python
- Django
- Django REST Framework
- PostgreSQL
- JWT Authentication
- drf-spectacular (Swagger Docs)

---

# Project Structure

```bash
leadmax-payment-system/
│
├── users/              # User management & authentication
├── accounts/           # Bank account management
├── payments/           # Payment transactions
├── core/               # Project settings & URLs
│
├── manage.py
├── requirements.txt
├── .env
└── README.md
```

---

# API Documentation

Swagger Documentation:

```txt
http://127.0.0.1:8000/api/docs/
```

---

# Installation & Setup

## 1. Clone Repository

```bash
git clone https://github.com/amehtacc/leadmax-payment-system
```

---

## 2. Move Into Project

```bash
cd leadmax-payment-system
```

---

## 3. Create Virtual Environment

### Windows

```bash
python -m venv venv
```

---

## 4. Activate Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

---

## 5. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# PostgreSQL Database Setup

## Create Database

Open PostgreSQL and run:

```sql
CREATE DATABASE leadmax_payment_system;
```

---

# Environment Variables

Create a `.env` file in the root directory:

```env
SECRET_KEY=your_secret_key

DEBUG=True

DB_NAME=leadmax_payment_system
DB_USER=postgres
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432
```

---

# Run Migrations

```bash
python manage.py makemigrations

python manage.py migrate
```

---

# Create Superuser

```bash
python manage.py createsuperuser
```

---

# Run Development Server

```bash
python manage.py runserver
```

Server:

```txt
http://127.0.0.1:8000/
```

---

# JWT Authentication

This project uses JWT Authentication.

## Token Expiry

| Token Type | Expiry |
|---|---|
| Access Token | 5 Minutes |
| Refresh Token | 1 Day |

---

# API Endpoints

# User APIs

| Method | Endpoint | Description |
|---|---|---|
| POST | `/api/users/register/` | Create User |
| POST | `/api/users/login/` | Login User |
| POST | `/api/users/refresh/` | Refresh Access Token |
| GET | `/api/users/profile/` | Get User Profile |
| GET | `/api/users/` | Get Users List |
| PUT | `/api/users/<id>/update/` | Update User |
| DELETE | `/api/users/<id>/delete/` | Delete User |

---

# Bank Account APIs

| Method | Endpoint | Description |
|---|---|---|
| POST | `/api/accounts/` | Add Bank Account |
| GET | `/api/accounts/list/` | Get User Bank Accounts |
| DELETE | `/api/accounts/<id>/delete/` | Delete Bank Account |
| POST | `/api/accounts/<id>/topup/` | Top-up Account Balance |

---

# Payment APIs

| Method | Endpoint | Description |
|---|---|---|
| POST | `/api/payments/` | Do Payment |
| GET | `/api/payments/transactions/` | Get Transaction History |

---

# Payment Flow

## Successful Payment
- Deduct amount from sender account
- Add amount to receiver account
- Mark transaction as SUCCESS

## Failed Payment
- Invalid account handling
- Insufficient balance handling
- Mark transaction as FAILED

---

# Security Features

- JWT Authentication
- Protected APIs
- Ownership Validation
- Secure Password Hashing
- Atomic Database Transactions
- Positive Amount Validation

---

# Business Logic Implemented

## Bank Accounts
- Maximum 3 accounts per user
- Unique account numbers
- Balance top-up support

## Payments
- Sender ownership verification
- Receiver validation
- Self-transfer prevention
- Insufficient balance checks
- Atomic payment processing

---

# Swagger Testing

1. Login using `/api/users/login/`
2. Copy access token
3. Click **Authorize** in Swagger
4. Enter:

```txt
YOUR_ACCESS_TOKEN
```

5. Test protected APIs

---

# Future Improvements

- Email Verification
- Password Reset
- Transaction Pagination
- Celery Background Tasks
- Docker Deployment
- Redis Caching
- Unit Testing
- CI/CD Pipeline

---

# Author

Aryan Mehta

---