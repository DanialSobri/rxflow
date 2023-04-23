import random
import json

class Booking:
   
    # Instance attribute
    def __init__(self,deliverytype:str="K"):
        self.rxtype = deliverytype # "K" = "Kaunter" | "DT" = "Drivetru"
        self.token = self.generateTokenKaunter() if deliverytype == "K" else self.generateTokenDrivetru()
        self.status = "CREATED"
    
    # Specific function
    def generateTokenKaunter(self):
        return self.generateToken(4000,4999)
    
    def generateTokenDrivetru(self):
        return self.generateToken(6000,6999)

    # Helper functions
    @classmethod
    def generateToken(self,min:int,max:int) -> int:
        return random.randrange(min,max,1)

    def checkTokenDB(self,token:int,DB):
        pass

    def getBookingAsJSON(self):
        return json.dumps(self.__dict__)

if __name__ == "__main__":
    from icecream import ic

    # Simple unit test
    ic(Booking.generateToken(0,10))

    mybooking = Booking()
    ic(mybooking.getBookingAsJSON())
    ic(mybooking.generateTokenKaunter())
    ic(mybooking.generateTokenDrivetru())
