from fastapi import APIRouter
from app.api.schemas import UserData

router = APIRouter()

# 先声明 service 变量
service = None


def set_service(service_instance):
    global service
    service = service_instance


@router.post("/summary")
def get_summary(user_data: UserData):
    return service.generate_summary(user_data)


@router.get("/history")
def history():
    return service.get_history()