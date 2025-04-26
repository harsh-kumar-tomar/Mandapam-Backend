from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from pydantic import BaseModel, EmailStr
from database import SessionLocal, engine
from models import Hotel as DBHotel, Base
from typing import Literal

Base.metadata.create_all(bind=engine)
app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Pydantic model
class HotelBase(BaseModel):
    hotel: str
    description: str
    phone_number: int
    email: EmailStr
    location: str
    capacity: int
    no_of_rooms: int
    rating: int
    wifi: bool
    parking: bool
    images: List[str]
    type: Literal["banquet_hall", "garden", "resort", "mandapam"]
    min_price: int
    max_price: int
    food_price: int

class HotelCreate(HotelBase):
    pass

class HotelOut(HotelBase):
    id: int
    class Config:
        orm_mode = True

@app.post("/hotels", response_model=HotelOut)
def create_hotel(hotel: HotelCreate, db: Session = Depends(get_db)):
    db_hotel = DBHotel(**hotel.dict())
    db.add(db_hotel)
    db.commit()
    db.refresh(db_hotel)
    return db_hotel

@app.get("/hotels", response_model=List[HotelOut])
def get_all_hotels(db: Session = Depends(get_db)):
    return db.query(DBHotel).all()

@app.get("/hotels/{hotel_id}", response_model=HotelOut)
def get_hotel(hotel_id: int, db: Session = Depends(get_db)):
    hotel = db.query(DBHotel).filter(DBHotel.id == hotel_id).first()
    if not hotel:
        raise HTTPException(status_code=404, detail="Hotel not found")
    return hotel

@app.delete("/hotels/{hotel_id}")
def delete_hotel(hotel_id: int, db: Session = Depends(get_db)):
    hotel = db.query(DBHotel).filter(DBHotel.id == hotel_id).first()
    if not hotel:
        raise HTTPException(status_code=404, detail="Hotel not found")
    db.delete(hotel)
    db.commit()
    return {"detail": "Hotel deleted"}

@app.put("/hotels/{hotel_id}", response_model=HotelOut)
def update_hotel(hotel_id: int, hotel_data: HotelCreate, db: Session = Depends(get_db)):
    hotel = db.query(DBHotel).filter(DBHotel.id == hotel_id).first()
    if not hotel:
        raise HTTPException(status_code=404, detail="Hotel not found")
    for key, value in hotel_data.dict().items():
        setattr(hotel, key, value)
    db.commit()
    db.refresh(hotel)
    return hotel
