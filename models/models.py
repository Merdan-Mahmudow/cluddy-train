from sqlalchemy import Column, Integer, MetaData, String, ARRAY
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = MetaData()

class Model(Base):
	__tablename__ = "model"
	id = Column(Integer, primary_key=True)
	name = Column(String)
	age = Column(Integer)
	city = Column(String, default="Южно-Сахалинск")
	weight = Column(Integer)
	height = Column(Integer)
	chest = Column(Integer)
	img = Column(ARRAY(String))