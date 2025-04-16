from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request
from fastapi.websockets import WebSocket
from manager import WebSocketManager



app = FastAPI()

templates = Jinja2Templates(
    directory="templates"
)

manager = WebSocketManager()

@app.get('/')
async def root(request : Request):
    return templates.TemplateResponse(
        request,
        'index.html',
        {}
    )
    
@app.websocket("/ws")
async def websocket_endpoint(websocket : WebSocket):
    await manager.connect(websocket)
    
