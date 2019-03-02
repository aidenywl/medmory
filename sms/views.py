from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseServerError, HttpResponse
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client

# Create your views here.

import json


def register_user(request):
    if request.method != 'POST':
        return HttpResponseServerError('wrong method used.')
    request_data = json.loads(request.body)

    # save the data into the database

    # communicate with twillo

    # return the code to be used.


@csrf_exempt
def sms_response(request):
    print(request)
    account_sid = 'AC60be041a5540d6b9083aea07443519d9'
    auth_token = 'ae409c66fcfbfd4c5f6a726b84bb64bf'
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
            body="Join Earth's mightiest heroes. Like Kevin Bacon.",
            from_='+12017545326',
            to='+18326204829'
        )
    print(message)
    return HttpResponse(str(message))
