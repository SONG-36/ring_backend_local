from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.exceptions import RequestValidationError

from app.api.routes_summary import router as summary_router, set_service
from app.infrastructure.in_memory_repo import InMemoryHealthRepository
from app.infrastructure.logging_repo import LoggingHealthRepository
from app.application.summary_service import SummaryService
from app.external.fake_llm import FakeLLMService
from app.utils.response import success
from fastapi import Request
from fastapi.responses import JSONResponse
from app.utils.response import success, fail, AppError
from app.core.logger import setup_logging
import logging

app = FastAPI()
setup_logging()
logger = logging.getLogger(__name__)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 创建具体实现
repository = InMemoryHealthRepository()
repository = LoggingHealthRepository()
llm_service = FakeLLMService()

# 注入到 Application
service = SummaryService(repository, llm_service)

# 注入到 API
set_service(service)

# 业务异常
@app.exception_handler(AppError)
async def app_error_handler(request: Request, exc: AppError):
    return JSONResponse(
        status_code=exc.http_status,
        content=fail(code=exc.code, message=exc.message),
    )

# 入参校验异常（Pydantic / FastAPI）
@app.exception_handler(RequestValidationError)
async def validation_error_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=422,
        content=fail(code=4220, message="参数校验失败", data=exc.errors()),
    )

# 未知异常兜底
@app.exception_handler(Exception)
async def unhandled_exception_handler(request: Request, exc: Exception):
    logger.error("Unhandled error", exc_info=True)
    return JSONResponse(
        status_code=500,
        content=fail(code=5000, message="系统错误，请稍后再试"),
    )


# 注册路由
app.include_router(summary_router)

@app.get("/health")
def health_check():
    return success({"status": "ok"})  # 使用统一响应