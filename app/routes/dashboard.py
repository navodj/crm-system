# app/routes/dashboard.py

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func
from app.database import get_db
from app import models
from app.auth import verify_token

router = APIRouter(prefix="/dashboard", tags=["Dashboard"])

@router.get("/")
def get_dashboard(db: Session = Depends(get_db), user = Depends(verify_token)):

    # ✅ total leads
    total_leads = db.query(models.Lead).count()

    # ✅ status counts
    new_leads = db.query(models.Lead).filter(models.Lead.status == "New").count()
    qualified_leads = db.query(models.Lead).filter(models.Lead.status == "Qualified").count()
    won_leads = db.query(models.Lead).filter(models.Lead.status == "Won").count()
    lost_leads = db.query(models.Lead).filter(models.Lead.status == "Lost").count()

    # ✅ deal values
    total_value = db.query(func.sum(models.Lead.deal_value)).scalar() or 0
    won_value = db.query(func.sum(models.Lead.deal_value))\
        .filter(models.Lead.status == "Won")\
        .scalar() or 0

    return {
        "total_leads": total_leads,
        "new_leads": new_leads,
        "qualified_leads": qualified_leads,
        "won_leads": won_leads,
        "lost_leads": lost_leads,
        "total_value": total_value,
        "won_value": won_value
    }