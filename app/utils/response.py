from fastapi import HTTPException
from typing import Any


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