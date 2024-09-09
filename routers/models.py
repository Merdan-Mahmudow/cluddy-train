from fastapi import APIRouter, Depends, UploadFile
from sqlalchemy import delete, insert, select
from db.db import get_async_session
from models.models import Model
from schemas import schemas as DTO
from sqlalchemy.ext.asyncio import AsyncSession
from .s3 import put_object




modelRouter = APIRouter()

@modelRouter.post('/')
async def model_add(img: UploadFile, session: AsyncSession = Depends(get_async_session)):
	put_object(img.filename)
	# stmt = insert(Model).values(modelDTO.model_dump())
	# await session.execute(stmt)
	# await session.commit()
	return img

@modelRouter.get('/')
async def all_models(session: AsyncSession = Depends(get_async_session)):
	query = select(Model)
	result = await session.execute(query)
	return result.mappings().all()

@modelRouter.get('/filter/{type}')
async def filetring(
	type: int, 
	city: str = "", 
	from_price: int = None, 
	to_price: int = None, 
	from_age: int = None, 
	to_age: int = None, 
	from_chest: int = None, 
	to_chest: int = None, 
	from_weight: int = None, 
	to_weight: int = None, 
	from_height: int = None, 
	to_height: int = None, 
	session: AsyncSession = Depends(get_async_session)):
	if type == 1:
		query = select(Model).where(Model.city == city)
		result = await session.execute(query)
		return result.mappings().all()
	# elif type == 2:
	# 	query = select(Model).where(Model.price >= from_price, Model.price <= to_price)
	# 	result = await session.execute(query)
	# 	return result.mappings().all()
	elif type == 3:
		query = select(Model).where(Model.age >= from_age, Model.age <= to_age)
		result = await session.execute(query)
		return result.mappings().all()
	elif type == 4:
		query = select(Model).where(Model.chest >= from_chest, Model.chest <= to_chest)
		result = await session.execute(query)
		return result.mappings().all()
	elif type == 5:
		query = select(Model).where(Model.weight >= from_weight, Model.weight <= to_weight)
		result = await session.execute(query)
		return result.mappings().all()
	elif type == 6:
		query = select(Model).where(Model.height >= from_weight, Model.whight <= to_weight)
		result = await session.execute(query)
		return result.mappings().all()
	elif type == 0:
		model = {
			"city": city,
			"from_age": from_age,
			"to_age": to_age,
			"from_chest": from_chest,
			"to_chest": to_chest,
			"from_weight": from_weight,
			"to_weight": to_weight,
			"from_height": from_height,
			"to_height": to_height,
		}
		for el in model:
			if model[el] is None:
				del model[el]
		query = select(Model).where(Model.city == model.city, Model.age >= model.from_age, Model.age <= model.to_age, Model.chest >= model.from_chest, Model.chest <= model.to_chest, Model.weight >= model.from_weight, Model.weight <= model.to_weight, Model.height >= model.from_height, Model.height <= model.to_height)
		result = await session.execute(query)
		return result.mappings().all()

@modelRouter.delete("/{id}")
async def delete_model(id: int, session: AsyncSession = Depends(get_async_session)):
	stmt = delete(Model).where(Model.id == id)
	await session.execute(stmt)
	await session.commit()
	return "Deleted from database"