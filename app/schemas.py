from pydantic import BaseModel
from typing import Optional
from datetime import datetime

# ---------------- LEAD ----------------
class LeadCreate(BaseModel):
    lead_name: str
    company_name: str
    email: str
    phone: str
    source: str
    assigned_to: str
    status: str
    deal_value: float


class LeadResponse(LeadCreate):
    id: int
    created_at: Optional[datetime]

    class Config:
        orm_mode = True


# ---------------- NOTE ----------------
class NoteCreate(BaseModel):
    content: str
    created_by: str


class NoteResponse(NoteCreate):
    id: int
    lead_id: int
    created_at: Optional[datetime]

    class Config:
        from_attributes = True


