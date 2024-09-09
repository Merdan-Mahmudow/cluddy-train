from fastapi import APIRouter

from .models import modelRouter

router = APIRouter()

router.include_router(modelRouter, prefix="/model", tags=["model"])