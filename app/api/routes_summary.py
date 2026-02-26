from fastapi import APIRouter
from app.api.schemas import UserData
from app.application.summary_service import generate_summary

router = APIRouter()

@router.post("/summary")
def get_summary(user_data: UserData):
    return generate_summary(user_data)