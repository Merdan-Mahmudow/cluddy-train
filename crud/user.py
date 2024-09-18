from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from db.db import get_async_session
from  schemas.schemas import User as userDTO
from models.users import User
from sqlalchemy import insert



