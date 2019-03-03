from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseServerError, HttpResponse
from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException
from django.conf import settings
from .tasks import send_reminder, test_task
from django.utils import timezone
import datetime
from .models import *
from twilio.base.exceptions import TwilioRestException
# Create your views here.
import json

from .forms import PatientForm, MedicationForm, ReminderForm


@csrf_exempt
def register_user(request):
    """
    Registers a user from the react frontend server.

    Request should contain patient and medication information.
    """
    print("HELLO")
    if request.method != 'POST':
        return HttpResponseServerError('wrong method used.')
    request_data = json.loads(request.body)

    patient_data = {
        'first_name': request_data['first_name'],
        'last_name': request_data['last_name'],
        'phone_number': request_data['phone_number'],
        'registration_date': timezone.now()
    }

    patient_instance = Patient.objects.create(first_name=patient_data['first_name'],
                                              last_name=patient_data['last_name'],
                                              phone_number=patient_data['phone_number'],
                                              registration_date=patient_data['registration_date'])

    print("before saving instance")
    print(patient_instance)
    patient_instance.save()
    print("saved instance")
    # retrieve the patient.
    patient = Patient.objects.filter(
        phone_number=patient_data['phone_number'])[0]
    print(patient)
    # Looping through the medications and saving to the database.
    all_medications = request_data['medications']
    # Register the patient's phone number with twilio
    try:
        _sms_register(patient_data['phone_number'])
    except TwilioRestException as err:
        print(err)
        pass

    print("The prescriptions received are: ", all_medications)

    for med in all_medications:
        medication_data = {
            'med_name': med['med_name'],
            'dosage': med['dosage'],
            'unit': med['dosage_unit'],
            'frequency': med['frequency'],
            'time_period': med['time_period']
        }
        med_instance = Medication.objects.create(
            med_name=medication_data['med_name'],
            dosage=medication_data['dosage'],
            unit=medication_data['unit'],
            frequency=medication_data['frequency'],
            time_period=medication_data['time_period'],
            patient_id=patient.id
        )
        med_instance.save()

        _create_reminders(patient_data, medication_data)

    return HttpResponse("OK")
    # save the data into the database

    # communicate with twillo

    # return the code to be used.


@csrf_exempt
def _sms_register(phone_num):
    # create client with credentials
    client = Client(settings.ACCOUNT_SID, settings.AUTH_TOKEN)
    # register user with phone_num
    validation_request = client.validation_requests \
        .create(
            friendly_name=phone_num,
            phone_number='+1' + phone_num
        )
    print(validation_request.friendly_name)
    return HttpResponse(str(validation_request.friendly_name))


def test_scheduling(request, message):
    for x in range(5):
        now = datetime.datetime.now()
        # remind every 10 seconds
        scheduled_medication_time = now + (datetime.timedelta(seconds=10) * x)
        # schedule task send_reminder
        test_task.schedule(args=(message,),
                           eta=scheduled_medication_time)
    return HttpResponse('scheduling complete')


def _create_reminders(patient, medication):
        # remind in 5 seconds
    now = datetime.datetime.now()
    scheduled_time = now + (datetime.timedelta(seconds=5))
    message = medication['dosage'] + medication['unit']
    # create reminder
    reminder_data = {
        'scheduled_medication_time': scheduled_time,
    }
    reminder_form = ReminderForm(reminder_data)
    # If the form is not valid, reject the request.
    if not reminder_form.is_valid():
        return HttpResponseServerError("Reminder data is not valid.")

    reminder_form.save()  # save to the database

    # schedule task send_reminder
    send_reminder.schedule(args=(patient, reminder_form.id, message,),
                           eta=scheduled_time)
    return


@csrf_exempt
def sms_response(request):
	message = json.loads(request.body)
	print(message)
	# create client with credentials
	client = Client(settings.ACCOUNT_SID, settings.AUTH_TOKEN)
    # send message
	message = client.messages \
        .create(
            body=message,
            from_=settings.ACCOUNT_NUMBER,
            to='+14159198310'
        )
	return HttpResponse(str(message))
