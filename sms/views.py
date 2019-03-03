from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseServerError, HttpResponse
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client
from django.conf import settings

# Create your views here.

import json


@csrf_exempt
def register_user(request):
    print("HELLO")
    if request.method != 'POST':
        return HttpResponseServerError('wrong method used.')
    request_data = json.loads(request.body)
    print(request_data)
    return HttpResponse("ok")
    # save the data into the database

    # communicate with twillo

    # return the code to be used.


@csrf_exempt
def sms_register(request, number):
	# create client with credentials
	client = Client(settings.ACCOUNT_SID, settings.AUTH_TOKEN)
	# register user with number
	validation_request = client.validation_requests \
        .create(
            friendly_name=number,
            phone_number='+1' + number
        )
	print(validation_request.friendly_name)
	return HttpResponse(str(validation_request.friendly_name))


@csrf_exempt
def sms_response(request):
    print(request)
	# create client with credentials
    client = Client(settings.ACCOUNT_SID, settings.AUTH_TOKEN)
	# send message
    message = client.messages \
        .create(
            body="Join Earth's mightiest heroes. Like Kevin Bacon.",
            from_=settings.ACCOUNT_NUMBER,
            to='+18326204829'
        )
    print(message)
    return HttpResponse(str(message))
