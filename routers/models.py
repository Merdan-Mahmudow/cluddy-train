from typing import List, Optional
from fastapi import APIRouter, Depends, File, UploadFile
from sqlalchemy import delete, insert, select
from db.db import get_async_session
from models.models import Model
from schemas import schemas as DTO
from sqlalchemy.ext.asyncio import AsyncSession
from .s3 import put_object, upload_file_to_s3




modelRouter = APIRouter()

@modelRouter.post('/')
async def model_add(
	name: Optional[str] = None,
    age: Optional[int] = None,
    city: Optional[str] = None,
    weight: Optional[int] = None,
    height: Optional[int] = None,
    chest: Optional[int] = None,
    phone: Optional[str] = None,
    cloth: Optional[str] = None,
    shoes: Optional[int] = None,
    hair: Optional[str] = None,
    appereance: Optional[str] = None,
    day_1_hour: Optional[int] = None,
    day_2_hour: Optional[int] = None,
    night_1_hour: Optional[int] = None,
    night_all: Optional[int] = None,
	img: List[UploadFile] = File(...), 
	session: AsyncSession = Depends(get_async_session)):
	images = await upload_file_to_s3(img)
	img_urls = []
	for image in images:
		img_urls.append(image["url"])
	print(img_urls)
	stmt = insert(Model).values(img=img_urls, name=name, age=age, city=city, weight=weight, height=height, chest=chest, phone=phone, cloth=cloth, shoes=shoes, hair=hair, appereance=appereance, day_1_hour=day_1_hour, day_2_hour=day_2_hour, night_1_hour=night_1_hour, night_all=night_all)
	await session.execute(stmt)
	await session.commit()
	return "added succesfully"

@modelRouter.put('/')
async def file_upload(file: List[UploadFile] = File(...)):
	return await upload_file_to_s3(file)

@modelRouter.get('/')
async def all_models(session: AsyncSession = Depends(get_async_session)):
	query = select(Model)
	result = await session.execute(query)
	return result.mappings().all()


@modelRouter.get('/filter/')
async def filtering(
	#type: int, 
	city: Optional[str] = None, 
	#from_price: Optional[int] = None, 
	#to_price: Optional[int] = None, 
	from_age: Optional[int] = None, 
	to_age: Optional[int] = None, 
	from_chest: Optional[int] = None, 
	to_chest: Optional[int] = None, 
	from_weight: Optional[int] = None, 
	to_weight: Optional[int] = None, 
	from_height: Optional[int] = None, 
	to_height: Optional[int] = None, 
	session: AsyncSession = Depends(get_async_session)):
	
	query = select(Model)

	if city:
		query = query.where(Model.city == city)
	
	#if from_price:
	#	query = query.where(Model.price >= from_price)
	#if to_price:
	#	query = query.where(Model.price <= to_price)
	
	if from_age:
		query = query.where(Model.age >= from_age)
	if to_age:
		query = query.where(Model.age <= to_age)
	
	if from_chest:
		query = query.where(Model.chest >= from_chest)
	if to_chest:
		query = query.where(Model.chest <= to_chest)
	
	if from_weight:
		query = query.where(Model.weight >= from_weight)
	if to_weight:
		query = query.where(Model.weight <= to_weight)
	
	if from_height:
		query = query.where(Model.height >= from_height)
	if to_height:
		query = query.where(Model.height <= to_height)
	
	result = await session.execute(query)
	return result.mappings().all()


@modelRouter.delete("/{id}")
async def delete_model(id: int, session: AsyncSession = Depends(get_async_session)):
	stmt = delete(Model).where(Model.id == id)
	await session.execute(stmt)
	await session.commit()
	return "Deleted from database"