"""Booking class contains business logics needed for the project

Returns:
    _type_: _description_
"""
import random
from faker import Faker
from booking import model

class Booking:
    
    # Helper functions
    def generateToken(self,min:int,max:int) -> int:
        return random.randrange(min,max,1)

    # Specific function
    def generateTokenKaunter(self) -> str:
        return str(self.generateToken(self,4000,4999))
    
    def generateTokenDrivetru(self) -> str:
        return str(self.generateToken(self,6000,6999))
    
    @classmethod
    def create_medicine(cls,items):
        return model.Medicine(
            items = items
            )
    
    @classmethod
    def create_patient(cls,name,telnumber,spnumber):
        return model.Patient(
            name = name,
            spnumber = spnumber,
            telnumber = telnumber
        )
    
    @classmethod
    def create_booking(cls,db,delivery,hospital,patient,medicines=[]):
        return model.Booking(
            id = len(db) + 1 ,
            token = cls.generateTokenKaunter(cls) if delivery=="K" else cls.generateTokenDrivetru(cls),
            delivery = delivery,
            status = "CREATED",
            hospital = hospital,
            patient = patient,
            medicines = medicines
        )
    
    @classmethod
    def create_fake_booking(cls,db):
        fake = Faker()
        patient = cls.create_patient(fake.name(),"+4915788217562","SP"+fake.msisdn()[:6])
        medicines = cls.create_medicine(items={"InsulinPen":"Novapen","GTN":"No","Sedut":"Yes"})
        delivery = "K" if len(db)%2==0 else "DT"
        return cls.create_booking(db,delivery,"HSAH",patient,medicines)