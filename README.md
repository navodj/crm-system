# CRM System

Full-stack CRM application for managing sales leads and notes.

## Tech Stack

### Backend
- **Python 3.10+** — runtime
- **FastAPI** — web framework
- **SQLAlchemy 2** — ORM
- **PyMySQL** — MySQL driver
- **Pydantic 2** — data validation
- **python-jose** — JWT auth
- **MySQL** — database

### Frontend
- **React 19** — UI library
- **React DOM 19** — rendering
- **Axios** — HTTP client with JWT interceptor
- **Tailwind CSS 4** — styling
- **Create React App** — build tooling

## Project Structure

```
crm-system/
│
├── backend/                   # (project root)
│   ├── app/
│   │   ├── main.py            # FastAPI entry point, table creation, router registration
│   │   ├── database.py        # SQLAlchemy engine & session
│   │   ├── models.py          # ORM models (Lead, Note)
│   │   ├── schemas.py         # Pydantic request/response schemas
│   │   ├── auth.py            # JWT creation & verification
│   │   ├── routes/
│   │   │   ├── leads.py       # CRUD endpoints for leads (JWT protected)
│   │   │   ├── notes.py       # Lead-scoped notes endpoints (JWT protected)
│   │   │   ├── auth.py        # Login endpoint (public)
│   │   │   └── dashboard.py   # (stub) dashboard stats
│   │   └── __init__.py
│   ├── requirements.txt       # Python dependencies
│   └── README.md
│
└── frontend/
    ├── public/
    │   └── index.html         # HTML template
    ├── src/
    │   ├── index.js           # React entry point
    │   ├── App.js             # Root component, auth-gated routing
    │   ├── index.css          # Global styles
    │   ├── api/
    │   │   └── api.js         # Axios instance with auto Bearer token interceptor
    │   └── pages/
    │       ├── Login.jsx      # Login form → JWT stored in localStorage
    │       ├── Dashboard.jsx  # Displays lead stats from /dashboard
    │       └── Leads.jsx      # Lists all leads from /leads
    ├── package.json           # Node dependencies & scripts
    └── package-lock.json
```

## API Endpoints

| Method | Endpoint             | Auth Required | Description            |
|--------|----------------------|---------------|------------------------|
| GET    | `/`                  | No            | Health check           |
| POST   | `/auth/login`        | No            | Login, returns JWT     |
| POST   | `/leads/`            | Yes           | Create a lead          |
| GET    | `/leads/`            | Yes           | List all leads         |
| GET    | `/leads/{id}`        | Yes           | Get a single lead      |
| PUT    | `/leads/{id}`        | Yes           | Update a lead          |
| DELETE | `/leads/{id}`        | Yes           | Delete a lead          |
| POST   | `/notes/lead/{id}`   | Yes           | Add a note to a lead   |
| GET    | `/notes/lead/{id}`   | Yes           | Get notes for a lead   |

### Auth Flow

1. `POST /auth/login` with `email` and `password`
2. Returns `{"access_token": "...", "token_type": "bearer"}`
3. Frontend stores token in `localStorage`; Axios interceptor auto-attaches it
4. Default credentials: `admin@example.com` / `password123`

## How to Run

### Prerequisites

- Python 3.10+
- Node.js 18+
- MySQL running on `localhost:3306`
- Database `crm_db` created

### Backend

```bash
cd crm-system
python -m venv .venv && .venv\Scripts\activate
pip install -r requirements.txt
mysql -u root -e "CREATE DATABASE IF NOT EXISTS crm_db;"
uvicorn app.main:app --reload
```

Server at `http://localhost:8000`. Interactive docs at `http://localhost:8000/docs`.

### Frontend

```bash
cd crm-system/frontend
npm install
npm start
```

App at `http://localhost:3000` — proxies API calls to `http://127.0.0.1:8000`.
