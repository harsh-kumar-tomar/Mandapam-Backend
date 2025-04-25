from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.types import JSON
from database import Base

class Hotel(Base):
    __tablename__ = "hotels"

    id = Column(Integer, primary_key=True, index=True)
    hotel = Column(String, nullable=False)
    description = Column(String)
    phone_number = Column(Integer)
    email = Column(String)
    location = Column(String)
    capacity = Column(Integer)
    no_of_rooms = Column(Integer)
    rating = Column(Integer)
    wifi = Column(Boolean)
    parking = Column(Boolean)
    images = Column(JSON)  
    type = Column(String)  
    min_price = Column(Integer)
    max_price = Column(Integer)
    food_price = Column(Integer)
