#!/usr/bin/env python
#-*- coding: utf-8 -*-
import boto3
session = boto3.session.Session()
s3 = session.client(
    service_name='s3',
    endpoint_url='https://storage.yandexcloud.net'
)

# # Создать новый бакет
# s3.create_bucket(Bucket='cluddy-bucket')

# # Загрузить объекты в бакет

## Из строки

def put_object(Key):
    s3.put_object(Bucket='cluddy-bucket', Key=Key, Body='TEST', StorageClass='COLD')

# ## Из файла
def upload_file_to_s3():
    s3.upload_file('this_script.py', 'cluddy-bucket', 'py_script.py')

# Получить список объектов в бакете
for key in s3.list_objects(Bucket='cluddy-bucket')["Contents"]:
    print(key)

# # Удалить несколько объектов
# forDeletion = [{'Key':'object_name'}, {'Key':'script/py_script.py'}]
# response = s3.delete_objects(Bucket='cluddy-bucket', Delete={'Objects': forDeletion})

# # Получить объект
# get_object_response = s3.get_object(Bucket='cluddy-bucket',Key='py_script.py')
# print(get_object_response['Body'].read())
