from typing import Optional

from fastapi import FastAPI

# uvicorn main:app --reload    서버 시작

app = FastAPI()

# 루트 엔드포인트 생성


@app.get("/")
async def root():
    return {"message": "Hello FastAPI"}
