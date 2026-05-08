from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.auth import create_access_token

router = APIRouter(prefix="/auth", tags=["Auth"])

# ✅ request body model
class LoginRequest(BaseModel):
    email: str
    password: str

# ✅ hardcoded user
fake_user = {
    "email": "admin@example.com",
    "password": "password123"
}

@router.post("/login")
def login(data: LoginRequest):

    if data.email != fake_user["email"] or data.password != fake_user["password"]:
        raise HTTPException(status_code=401, detail="Invalid email or password")

    token = create_access_token({"sub": data.email})

    return {
        "access_token": token,
        "token_type": "bearer"
    }