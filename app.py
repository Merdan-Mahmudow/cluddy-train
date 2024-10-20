from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers.routers import router

app = FastAPI()

origins = ["https://angels-agency.ru", "https://backend.skyrodev.ru", "https://cluddy.skyrodev.ru", "http://localhost:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS", "DELETE", "PATCH", "PUT"],
    allow_headers=["Content-Type", "Set-Cookie", "Access-Control-Allow-Headers", "Access-Control-Allow-Origin",
                   "Authorization"],
)



app.include_router(router)