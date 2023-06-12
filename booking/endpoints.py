from fastapi import APIRouter, Depends, HTTPException
from booking import model
from booking.booking import Booking
from booking.notification import Notification
from config import settings

# from ..dependencies import get_token_header

router = APIRouter(
    prefix="/booking",
    tags=["Booking"],
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
    # Save to DB
    db[booking.id] = booking
    # Send token to patient
    telnumber,name = booking.patient.telnumber,booking.patient.name
    # TODO Messaging.send_message_token(telnumber,name,booking.token,"05/01/2023")
    return booking

# Create a new booking and add it to the database
@router.post("/create/fake", response_model=model.Booking)
def create_fake_booking():
    booking = Booking.create_fake_booking(db)
    # Save to DB
    db[booking.id] = booking
    # Send token to patient
    telnumber,name = booking.patient.telnumber,booking.patient.name
    # TODO Messaging.send_message_token(telnumber,name,booking.token,"05/01/2023")
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

# Notification
# Send notification through Whatsapp
@router.post("/approve/{booking_id}",tags=["Notification"])
async def send_notification(booking_id:int,approve:bool=True):
    if booking_id not in db:
        raise HTTPException(status_code=404, detail="Item not found")
    # Get booking
    booking = db.get(booking_id)
    # Send token to patient
    telnumber,name = booking.patient.telnumber,booking.patient.name

    if approve:
        mynotification = Notification.send_token(telnumber,name,booking.token,"05/01/2023")

    return mynotification