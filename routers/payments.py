import json
from typing import List
import uuid
from fastapi import APIRouter, HTTPException, Request, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import requests
import config

templates = Jinja2Templates(directory="templates")


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
        
		
@paymentRouter.get('/payment')
async def hello(request: Request, amount: str, currency: str, userId: str, chatId: str, adminChatId: str, modelData: str):
    try:
        response = await create_invoice(amount, currency)
        result = response["result"]
        return templates.TemplateResponse("payments.html", 
                                   {"request": request, "data": result, "user": {"chatId": chatId, "userId": userId, "admin":  adminChatId}, "model": json.loads(modelData)})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@paymentRouter.post('/create-invoice')
async def create_invoice(amount: str, currency: str):
	url = "https://api.cryptocloud.plus/v2/invoice/create?locale=ru"
	headers = {
		"Authorization": f"Token {config.API_KEY}",
		"Content-Type": "application/json"
	}
	data = {
			"amount": amount,
			"shop_id": f"{config.SHOP_ID}",
			"currency": f"{currency}",
			"email": "softprank@gmail.com",
		}
	response = requests.post(url, headers=headers, json=data)

	return response.json()

@paymentRouter.get("/payment_status")
async def get_payment_status(invoice_id: str):
	url = f"https://api.cryptocloud.plus/v2/invoice/merchant/info"
	headers = {
		"Authorization": f"Token {config.API_KEY}",
		"Content-Type": "application/json"
	}
	data = {"uuids": [invoice_id]}
	response = requests.post(url, headers=headers, json=data)
	return response.json()