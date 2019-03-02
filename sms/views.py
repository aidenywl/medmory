from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseServerError, HttpResponse
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client

# Create your views here.

import json


def register_user(request):
    print("HELLO")
    if request.method != 'POST':
        return HttpResponseServerError('wrong method used.')
    request_data = json.loads(request.body)

    # save the data into the database

    # communicate with twillo

    # return the code to be used.


@csrf_exempt
def sms_response(request):
    account_sid = 'AC7dca0086bf0fb3233c8a919a2deebd2e'
    auth_token = '8d5263c2694afda8113c0e7901227dba'
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
            body="Join Earth's mightiest heroes. Like Kevin Bacon.",
            from_='+12017545326',
            to='+18326204829'
        )
    print(message.sid)
    return HttpResponse(str(message.sid))
