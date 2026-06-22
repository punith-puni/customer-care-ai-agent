from fastapi import FastAPI

from routes.chat import router as chat_router
from routes.orders import router as order_router
from routes.admin import router as admin_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Customer Care AI Agent")
app.include_router(admin_router)
app.include_router(chat_router)
app.include_router(order_router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/")
def home():
    return {
        "message": "Customer Care AI Agent is running"
    }