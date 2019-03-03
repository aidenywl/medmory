from twilio.rest import Client
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings


@csrf_exempt
def send_message(phone_number, message):
    # create client with credentials
    client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
    # send message
    message = client.messages \
        .create(
            body=message,
            from_=settings.ACCOUNT_NUMBER,
            to='+' + phone_number
        )
    print(message)
