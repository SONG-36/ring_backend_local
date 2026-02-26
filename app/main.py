from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes_summary import router as summary_router, set_service
from app.infrastructure.in_memory_repo import InMemoryHealthRepository
from app.infrastructure.logging_repo import LoggingHealthRepository
from app.application.summary_service import SummaryService
from app.external.fake_llm import FakeLLMService

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 创建具体实现
repository = InMemoryHealthRepository()
#repository = LoggingHealthRepository()
llm_service = FakeLLMService()

# 注入到 Application
service = SummaryService(repository, llm_service)

# 注入到 API
set_service(service)

app.include_router(summary_router)

@app.get("/health")
def health_check():
    return {"status": "ok"}