# app/routes/notes.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app import models, schemas
from app.auth import verify_token

router = APIRouter(prefix="/notes", tags=["Notes"])


# ✅ ADD NOTE
@router.post("/lead/{lead_id}", response_model=schemas.NoteResponse)
def add_note(lead_id: int, note: schemas.NoteCreate, db: Session = Depends(get_db), user=Depends(verify_token)):
    # check if lead exists
    lead = db.query(models.Lead).filter(models.Lead.id == lead_id).first()
    if not lead:
        raise HTTPException(status_code=404, detail="Lead not found")

    new_note = models.Note(
        lead_id=lead_id,
        content=note.content,
        created_by=note.created_by
    )

    db.add(new_note)
    db.commit()
    db.refresh(new_note)

    return new_note


# ✅ GET NOTES FOR A LEAD
@router.get("/lead/{lead_id}", response_model=list[schemas.NoteResponse])
def get_notes(lead_id: int, db: Session = Depends(get_db), user=Depends(verify_token)):
    notes = db.query(models.Note).filter(models.Note.lead_id == lead_id).all()

    return notes
