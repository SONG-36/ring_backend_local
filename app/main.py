from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes_summary import router as summary_router

app = FastAPI()

# 允许前端访问（开发阶段）
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 注册路由
app.include_router(summary_router)

@app.get("/health")
def health_check():
    return {"status": "ok"}