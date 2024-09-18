from fastapi import APIRouter, WebSocket, WebSocketDisconnect

paymentRouter = APIRouter()

class ConnectionManager:
    def __init__(self):
        self.active_connections: list[WebSocket] = []
    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    async def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def send_personal_message(self, message: str, websocket: WebSocket):
        await websocket.send_text(message)

    async def broadcast(self, message: str):
        for connection in self.active_connections:
            await connection.send_text(message)
            print(connection)


manager = ConnectionManager()
@paymentRouter.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            print(data)
            await manager.broadcast("hello")
    except WebSocketDisconnect:
        await manager.disconnect(websocket)
        
		
@paymentRouter.get('/hello')
async def hello():
    return "hello"