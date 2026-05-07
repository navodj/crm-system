from fastapi import FastAPI
from app.database import engine
from app import models
from app.routes import leads
from app.routes import notes
from app.routes import dashboard
from app.routes import auth

app = FastAPI()
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