from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from twilio.twiml.messaging_response import MessagingResponse
# Create your views here.


@csrf_exempt
def sms_response(request):
    # start our TwiML response
    resp = MessagingResponse()

    # add a text message
    msg = resp.message("Check out this sweet owl!")

    return HttpResponse(str(resp))
