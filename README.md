# CRM System — Backend API

## Folder Structure

```
crm-system/
│── app/
│   ├── main.py              # FastAPI app entry point, table creation, router registration
│   ├── database.py           # SQLAlchemy engine, session, Base declarative class
│   ├── models.py             # ORM models (Lead, Note)
│   ├── schemas.py            # Pydantic schemas for request/response validation
│   ├── auth.py               # (stub) planned authentication logic
│   ├── routes/
│   │   ├── leads.py          # CRUD endpoints for leads
│   │   ├── notes.py          # Endpoints for notes (scoped to a lead)
│   │   ├── auth.py           # (stub) planned auth routes
│   │   └── dashboard.py      # (stub) planned dashboard routes
│   └── __init__.py
│── requirements.txt          # Python dependencies
└── README.md
```

## What It Does

A RESTful API for managing sales leads and notes. Built with FastAPI and SQLAlchemy, backed by a MySQL database.

### Models

- **Lead** — id, lead_name, company_name, email, phone, source, assigned_to, status, deal_value, created_at, updated_at
- **Note** — id, lead_id (FK → leads), content, created_by, created_at

### API Endpoints

| Method | Endpoint             | Description            |
|--------|----------------------|------------------------|
| GET    | `/`                  | Health check           |
| POST   | `/leads/`            | Create a lead          |
| GET    | `/leads/`            | List all leads         |
| GET    | `/leads/{id}`        | Get a single lead      |
| PUT    | `/leads/{id}`        | Update a lead          |
| DELETE | `/leads/{id}`        | Delete a lead          |
| POST   | `/notes/lead/{id}`   | Add a note to a lead   |
| GET    | `/notes/lead/{id}`   | Get notes for a lead   |

## How to Use

### Prerequisites

- Python 3.10+
- MySQL running on `localhost:3306`
- A database named `crm_db` created beforehand

### Setup

```bash
# 1. Clone and enter the project
cd crm-system

# 2. (Optional) Create a virtual environment
python -m venv .venv
.venv\Scripts\activate   # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Make sure MySQL is running and crm_db exists
mysql -u root -e "CREATE DATABASE IF NOT EXISTS crm_db;"

# 5. Run the server
uvicorn app.main:app --reload
```

The server starts at `http://localhost:8000`. Interactive API docs are at `http://localhost:8000/docs`.

### Database

Configured in `app/database.py` — defaults to `mysql+pymysql://root:@localhost:3306/crm_db`. Tables are auto-created on startup via `models.Base.metadata.create_all()`.
