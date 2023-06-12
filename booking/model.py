"""
 Approached used is by assigning each booking to a patient name, 
 without save any patient data. With this come following risks:
 - Need to check for duplicate booking made by the same person
 - Challeging to provide insight for each individual patient
 - As the mnumber of booking grow, it become more complicated to
 filter  booking made by a patient.
 - Problems when data entered not right
 .....................
 last updated May 2023 
"""
from pydantic import BaseModel
from typing import Optional

class Patient(BaseModel):
    name: str
    spnumber: str
    telnumber: str

class Medicine(BaseModel):
    items: Optional[dict]

class Booking(BaseModel):
    id: int
    token: str
    delivery: str
    status: str = "IDLE"
    hospital: str = "HSAH"
    patient: Patient
    medicines: Medicine

    # class Config:
    #     schema_extra = {
    #         "example": {
    #             "id" : 1,
    #             "token" : "4000",
    #             "delivery" : "K",
    #             "status" : "CREATED",
    #             "hospital" : "HSAH",
    #             "patient": {
    #                 "name": "Mad Mustaman",
    #                 "spnumber": "SP1233445",
    #                 "telnumber": "+6013456789"
    #             }

    #         }
    #     }

class Notification(BaseModel):
    
    message: str
    sentat: str
    telnumber: str
    status: str
