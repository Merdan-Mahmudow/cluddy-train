#!/usr/bin/env python
#-*- coding: utf-8 -*-
import io
from typing import List
import uuid
import boto3
from fastapi import UploadFile
from botocore.exceptions import NoCredentialsError

session = boto3.session.Session()
s3 = session.client(
    service_name='s3',
    endpoint_url='https://storage.yandexcloud.net'
)

# # Создать новый бакет
# s3.create_bucket(Bucket='cluddy-bucket')

# # Загрузить объекты в бакет

def put_object(Key):
    s3.put_object(Bucket='cluddy-bucket', Key=Key, Body='TEST', StorageClass='COLD')

async def get_url(file: List[UploadFile]):
	uploded_files = []
	filenames = []
	file_urls = []
	for f in file:
		file_content = await f.read()
		f.filename = str(uuid.uuid4()) + ".jpg"
		filenames.append(f.filename)
		s3.upload_fileobj(
			Fileobj=io.BytesIO(file_content),
			Bucket='cluddy-bucket',
			Key=f.filename
		)
		uploded_files.append({"filename": f.filename, "status": "uploaded"})
	async def get(img_url):
		return ["https://storage.yandexcloud.net/cluddy-bucket/" + uploded_files[f]["filename"] for f in range(len(uploded_files))]
	return await get(filenames)
		

# ## Из файла
async def upload_file_to_s3(file: List[UploadFile]):
	uploded_files = []
	filenames = []
	file_urls = []
	for f in file:
		file_content = await f.read()
		f.filename = str(uuid.uuid4()) + ".jpg"
		filenames.append(f.filename)
		s3.upload_fileobj(
			Fileobj=io.BytesIO(file_content),
			Bucket='cluddy-bucket',
			Key=f.filename
		)
		uploded_files.append({"filename": f.filename, "status": "uploaded"})
	async def get_url_from_s3(files: List[str]):
		for f in files:
			url = s3.generate_presigned_url(
				ClientMethod='get_object',
				Params={'Bucket': 'cluddy-bucket', 'Key': f}
			)
			file_urls.append({"filename": f, "url": url})
		return file_urls		
	return await get_url_from_s3(filenames)


# Получить список объектов в бакете
# for key in s3.list_objects(Bucket='cluddy-bucket')["Contents"]:
#     print(key)

# # Удалить несколько объектов
# forDeletion = [{'Key':'object_name'}, {'Key':'script/py_script.py'}]
# response = s3.delete_objects(Bucket='cluddy-bucket', Delete={'Objects': forDeletion})

# # Получить объект
# get_object_response = s3.get_object(Bucket='cluddy-bucket',Key='py_script.py')
# print(get_object_response['Body'].read())
