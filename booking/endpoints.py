from fastapi import APIRouter, Depends, HTTPException
from booking.Booking import Booking  
from booking import model
from config import settings

# from ..dependencies import get_token_header

router = APIRouter(
    prefix="/booking",
    tags=["booking"],
    # dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)

# Fake DB
db = {}

# CRUD Booking
# Read all bookings in db
@router.get("/all")
async def read_bookings():
    return list(db.values())

# Read a booking by id
@router.get("/{booking_id}",response_model=model.Booking)
async def get_booking(booking_id:int):
    if booking_id in db:
        return db.get(booking_id)
    raise HTTPException(status_code=404, detail="Item not found")

# Create a new booking and add it to the database
@router.post("/create/", response_model=model.Booking)
def create_booking(delivery,hospital,patient:model.Patient):
    booking = Booking.create_booking(db,delivery,hospital,patient)
    db[booking.id] = booking
    return booking

# Create a new booking and add it to the database
@router.post("/create/fake", response_model=model.Booking)
def create_fake_booking():
    booking = Booking.create_fake_booking(db)
    db[booking.id] = booking
    return booking

# Update an item by id
@router.put("/update/{booking_id}",response_model=model.Booking)
async def update_booking(booking_id:int, booking:model.Booking):
    if booking_id in db:
        db[booking_id] = booking
        return booking
    raise HTTPException(status_code=404, detail="Item not found")

# Delete an item by id
@router.delete("/{booking_id}")
async def delete_booking(booking_id:int):
    if booking_id in db:
        del db[booking_id]
        return None
    raise HTTPException(status_code=404, detail="Item not found")