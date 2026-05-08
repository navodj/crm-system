from fastapi import FastAPI
from app.database import engine
from app import models
from app.routes import leads
from app.routes import notes
from app.routes import dashboard
from app.routes import auth
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# ✅ CORS CONFIGURATION
origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],   # allows GET, POST, PUT, DELETE
    allow_headers=["*"],   # allows all headers
)
app.include_router(notes.router)
app.include_router(dashboard.router)
app.include_router(auth.router)



# ✅ create tables
models.Base.metadata.create_all(bind=engine)

# ✅ include routers AFTER app is defined
app.include_router(leads.router)

@app.get("/")
def root():
    return {"message": "CRM API running"}