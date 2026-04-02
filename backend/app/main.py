from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers.todos import router as todos_router

app = FastAPI(title="Todo App API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(todos_router)


@app.get("/api/health")
async def health_check():
    return {"status": "healthy"}
