# app/routes/leads.py

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app import models, schemas
from app.auth import verify_token
from fastapi import HTTPException


router = APIRouter(prefix="/leads", tags=["Leads"])

# CREATE LEAD
@router.post("/", response_model=schemas.LeadResponse)
def create_lead(lead: schemas.LeadCreate, db: Session = Depends(get_db), user=Depends(verify_token)):
    new_lead = models.Lead(**lead.dict())
    db.add(new_lead)
    db.commit()
    db.refresh(new_lead)
    return new_lead


# GET ALL LEADS
@router.get("/", response_model=list[schemas.LeadResponse])
def get_leads(db: Session = Depends(get_db),user=Depends(verify_token)):
    return db.query(models.Lead).all()



# GET SINGLE LEAD
@router.get("/{lead_id}", response_model=schemas.LeadResponse)
def get_lead(lead_id: int, db: Session = Depends(get_db), user=Depends(verify_token)):
    lead = db.query(models.Lead).filter(models.Lead.id == lead_id).first()

    if not lead:
        raise HTTPException(status_code=404, detail="Lead not found")

    return lead

# UPDATE LEAD
@router.put("/{lead_id}")
def update_lead(
    lead_id: int,
    lead: schemas.LeadCreate,
    db: Session = Depends(get_db),
    user=Depends(verify_token)
):
    existing = db.query(models.Lead).filter(models.Lead.id == lead_id).first()

    if not existing:
        raise HTTPException(status_code=404, detail="Lead not found")

    for key, value in lead.dict().items():
        setattr(existing, key, value)

    db.commit()

    return {"message": "Lead updated"}


# DELETE LEAD
@router.delete("/{lead_id}")
def delete_lead(
    lead_id: int,
    db: Session = Depends(get_db),
    user=Depends(verify_token)
):
    lead = db.query(models.Lead).filter(models.Lead.id == lead_id).first()

    if not lead:
        raise HTTPException(status_code=404, detail="Lead not found")

    db.delete(lead)
    db.commit()

    return {"message": "Deleted"}
