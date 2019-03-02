from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseServerError, HttpResponse
from twilio.twiml.messaging_response import MessagingResponse
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
        # start our TwiML response
    resp = MessagingResponse()

    # add a text message
    msg = resp.message("Check out this sweet owl!")

    return HttpResponse(str(resp))
