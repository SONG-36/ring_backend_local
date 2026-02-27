from fastapi import HTTPException
from typing import Any, Optional

class AppError(Exception):
    """业务异常：用于主动抛出，并由全局异常处理统一返回"""
    def __init__(self, code: int = 4000, message: str = "error", http_status: int = 400):
        self.code = code
        self.message = message
        self.http_status = http_status
        super().__init__(message)

def success(data: Any = None, message: str = "success"):
    return {
        "code": 0,
        "message": message,
        "data": data
    }


def error(message: str = "error", code: int = 500):
    raise HTTPException(status_code=code, detail={
        "code": code,
        "message": message,
        "data": None
    })

def fail(code: int = 4000, message: str = "error", data: Any = None):
    return {"code": code, "message": message, "data": data}