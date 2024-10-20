from fastapi import APIRouter

from .models import modelRouter
from .payments import paymentRouter
from .users import userRouter




router = APIRouter()

router.include_router(modelRouter, prefix="/model", tags=["model"])
router.include_router(paymentRouter, prefix="/payment", tags=["payment"])
router.include_router(userRouter, prefix="/user", tags=["user"])

