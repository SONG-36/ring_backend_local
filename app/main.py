from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError

import logging

from app.api.routes_summary import router as summary_router, set_service
from app.application.summary_service import SummaryService
from app.infrastructure.in_memory_repo import InMemoryHealthRepository
from app.infrastructure.logging_repo import LoggingHealthRepository
from app.external.fake_llm import FakeLLMService
from app.utils.response import success, fail, AppError
from app.core.logger import setup_logging
from app.core.settings import get_settings


# ------------------------
# 初始化核心能力
# ------------------------

setup_logging()
logger = logging.getLogger(__name__)
settings = get_settings()

app = FastAPI(title=settings.APP_NAME)


# ------------------------
# CORS 配置（可配置）
# ------------------------

app.add_middleware(
    CORSMiddleware,
    allow_origins=[settings.CORS_ORIGINS],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ------------------------
# 依赖组装（Composition Root）
# ------------------------

def create_repository():
    if settings.REPOSITORY_TYPE == "memory":
        return InMemoryHealthRepository()
    elif settings.REPOSITORY_TYPE == "logging":
        return LoggingHealthRepository()
    else:
        raise RuntimeError("Unknown repository type")


def create_llm_service():
    # 阶段 1 先用 fake
    return FakeLLMService()


repository = create_repository()
llm_service = create_llm_service()

service = SummaryService(repository, llm_service)
set_service(service)


# ------------------------
# 全局异常处理
# ------------------------

@app.exception_handler(AppError)
async def app_error_handler(request: Request, exc: AppError):
    return JSONResponse(
        status_code=exc.http_status,
        content=fail(code=exc.code, message=exc.message),
    )


@app.exception_handler(RequestValidationError)
async def validation_error_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=422,
        content=fail(code=4220, message="参数校验失败", data=exc.errors()),
    )


@app.exception_handler(Exception)
async def unhandled_exception_handler(request: Request, exc: Exception):
    logger.error("Unhandled error", exc_info=True)
    return JSONResponse(
        status_code=500,
        content=fail(code=5000, message="系统错误，请稍后再试"),
    )


# ------------------------
# 注册路由
# ------------------------

app.include_router(summary_router)


@app.get("/health")
def health_check():
    return success({"status": "ok"})