from fastapi import FastAPI
from routes import users, code, ai
from websocket import websocket_endpoint
import uvicorn

app = FastAPI()

# Include API routes
app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(code.router, prefix="/code", tags=["code"])
app.include_router(ai.router, prefix="/ai", tags=["ai"])

# WebSocket endpoint
app.websocket("/ws")(websocket_endpoint)


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)