from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseServerError, HttpResponse
from twilio.rest import Client
from django.conf import settings
from .tasks import send_reminder, test_task
import datetime
# Create your views here.

import json

from .forms import PatientForm, MedicationForm


@csrf_exempt
def register_user(request):
    print("HELLO")
    if request.method != 'POST':
        return HttpResponseServerError('wrong method used.')
    request_data = json.loads(request.body)

    patient_data = {
        'first_name': request_data['first_name'],
        'last_name': request_data['last_name'],
        'phone_number': request_data['phone_number']
    }

    patientForm = PatientForm(patient_data)
    # If the form is not valid, reject the request.
    if not patientForm.is_valid():
        return HttpResponseServerError("Patient data is not valid.")

    patientForm.save()  # save to the database

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

def test_scheduling(request, message):
    for x in range(5):
        now = datetime.datetime.now()
        # remind every 5 mins
        scheduled_medication_time = now + (datetime.timedelta(seconds=10) * x)
        # schedule task send_reminder
        test_task.schedule(args=(message,),
                           eta=scheduled_medication_time)
    return HttpResponse('scheduling complete')



def _create_reminders(patient, medication):
    for x in range(5):
        now = datetime.datetime.now()
        # remind every 5 mins
        scheduled_medication_time = now + (datetime.timedelta(seconds=10) * x)
        message = medication['dosage'] + medication['unit']
        # schedule task send_reminder
        send_reminder.schedule(args=(patient['phone_number'], message,),
                               eta=scheduled_medication_time)
    return


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
