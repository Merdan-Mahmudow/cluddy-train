from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
from schemas.schemas import User as userDTO
from sqlalchemy.ext.asyncio import AsyncSession
from db.db import get_async_session
from models.models import User
from sqlalchemy import delete, insert, select, update


userRouter = APIRouter()

@userRouter.post('/')
async def create_user(user: userDTO, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(User).values(user.dict())
    await session.execute(stmt)
    await session.commit()
    return "added succesfully"

@userRouter.get('/{chat_id}', response_model=userDTO)
async def all_users(chat_id: str, session: AsyncSession = Depends(get_async_session)):
    query = select(User).where(User.chatID == chat_id)
    result = await session.execute(query)
    data = result.mappings().first()
    if data == None:
        return JSONResponse(status_code=404, content={"detail": "Not found"})
    else:
        return data["User"]

@userRouter.patch('/{id}')
async def update_user(id: str, user: userDTO, session: AsyncSession = Depends(get_async_session)):
    query = update(User).where(User.chatID == id).values(user.dict())
    await session.execute(query)
    await session.commit()
    return "updated succesfully"

@userRouter.delete("/{id}")
async def delete_user(id: str, session: AsyncSession = Depends(get_async_session)):
    stmt = delete(User).where(User.chatID == id)
    await session.execute(stmt)
    await session.commit()
    return "Deleted from database"