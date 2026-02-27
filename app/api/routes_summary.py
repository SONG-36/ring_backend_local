from fastapi import APIRouter
from app.api.schemas import UserData
from app.utils.response import success

router = APIRouter()

# 先声明 service 变量
service = None


def set_service(service_instance):
    global service
    service = service_instance


@router.post("/summary")
def get_summary(user_data: UserData):
    result = service.generate_summary(user_data)
    return success(result)


@router.get("/history")
def history():
    return success(service.get_history())