from fastapi import APIRouter, HTTPException
from app.auth import create_access_token

router = APIRouter(prefix="/auth", tags=["Auth"])

# ✅ hardcoded user
fake_user = {
    "email": "admin@example.com",
    "password": "password123"
}


@router.post("/login")
def login(email: str, password: str):

    # ✅ check credentials
    if email != fake_user["email"] or password != fake_user["password"]:
        raise HTTPException(status_code=401, detail="Invalid email or password")

    # ✅ create token
    token = create_access_token({"sub": email})

    return {
        "access_token": token,
        "token_type": "bearer"
    }
