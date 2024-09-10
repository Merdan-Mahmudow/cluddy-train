from sqlalchemy import Column, Integer, MetaData, String, ARRAY
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = MetaData()

class Model(Base):
	__tablename__ = "model"
	id = Column(Integer, primary_key=True)
	name = Column(String, nullable=True)
	age = Column(Integer, nullable=True)
	city = Column(String, nullable=True, default="Южно-Сахалинск")
	weight = Column(Integer, nullable=True)
	height = Column(Integer, nullable=True)
	chest = Column(Integer, nullable=True)
	img = Column(ARRAY(String), nullable=True)
	phone = Column(String, nullable=True)
	cloth = Column(String, nullable=True)
	shoes = Column(Integer, nullable=True)
	hair = Column(String, nullable=True)
	appereance = Column(String, nullable=True)
	day_1_hour = Column(Integer, nullable=True)
	day_2_hour = Column(Integer, nullable=True)
	night_1_hour = Column(Integer, nullable=True)
	night_all = Column(Integer, nullable=True)


	