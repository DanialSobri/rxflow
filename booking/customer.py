import json
from booking import Booking

class Customer:

    def __init__(self, name:str, sp_number:str, tel_number:str):
        self.name = name
        self.sp_number = sp_number
        self.tel_number = tel_number
        self.bookings = {}
    
    def getCustomerAsJSON(self):
        customer = {}
        customer["name"] = self.name
        customer["sp_number"] = self.sp_number
        customer["tel_number"] = self.tel_number
        customer["bookings"] = {}   
        for booking in self.bookings:
            customer["bookings"][booking] = self.bookings.get(booking).getBookingAsJSON()
        return customer

    def addBooking(self,new_booking:Booking):
        booking_id=len(self.bookings)
        self.bookings[booking_id] = new_booking
        return booking_id

    def getBookings(self)->dict:
        return self.bookings
    
    def getBooking(self,booking_id:str):
        return self.bookings.get(booking_id)
    
    def updateBooking(self, booking_id:str):
        return self.bookings.get(booking_id)

if __name__ == "__main__":
    from icecream import ic 
    cust1 = Customer("Max Musterman","SP2892893","+6013456789")
    ic(cust1.getCustomerAsJSON())
    ic(cust1.getBookings())
    ic(cust1.addBooking(Booking()))
    ic(cust1.addBooking(Booking("DT")))
    ic(cust1.getBooking(0).getBookingAsJSON())
    ic(cust1.getCustomerAsJSON())
