from twilio.rest import Client
from django.views.decorators.csrf import csrf_exempt
from .credentials import *


@csrf_exempt
def send_message(phone_number, message):
    # create client with credentials
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    # send message
    message = client.messages \
        .create(
            body=message,
            from_=ACCOUNT_NUMBER,
            to='+' + phone_number
        )
    print(message)
