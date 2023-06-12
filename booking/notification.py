import requests
from config import settings

class Notification:
    
    @classmethod
    def send_token(cls,telnumber:str,name:str,bookingtoken:str,date:str):
        # Set the endpoint URL and the access token
        url = "https://graph.facebook.com/v16.0/106511229099238/messages"
        token = settings.WSTOKEN

        # Set the headers with the authorization and content type
        headers = {
            "Authorization": "Bearer " + token,
            "Content-Type": "application/json"
        }

        # Set the payload with the phone number ID, recipient phone number and template object
        payload = { 
            "messaging_product": "whatsapp", 
            "to": "4915788217562", 
            "type": "template", 
            "template": { 
                "name": "booking_token", 
                "language": { "code": "ms" },
                "components": [
                {
                "type": "body",
                "parameters": [
                    {
                    "type": "text",
                    "text": name
                    },
                    {
                    "type": "text",
                    "text": bookingtoken
                    },
                    {
                    "type": "text",
                    "text": date
                    }
                ]
                }
            ]
            },

        }

        # Make a POST request and print the response 
        response = requests.post(url, headers=headers, json=payload)
        return response.json()
