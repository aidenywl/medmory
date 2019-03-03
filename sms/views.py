from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseServerError, HttpResponse
from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException
from .credentials import *
from .tasks import send_reminder, test_task
from django.utils import timezone
import datetime
from .models import *
from twilio.base.exceptions import TwilioRestException
# Create your views here.
import json

from .forms import PatientForm, MedicationForm, ReminderForm

import logging
import os
from django.views.generic import View
from django.conf import settings

class FrontendAppView(View):
    """
    Serves the compiled frontend entry point (only works if you have run `yarn
    run build`).
    """

    def get(self, request):
        try:
            with open(os.path.join(settings.REACT_APP_DIR, 'build', 'index.html')) as f:
                return HttpResponse(f.read())
        except FileNotFoundError:
            logging.exception('Production build of app not found')
            return HttpResponse(
                """
                This URL is only used when you have built the production
                version of the app. Visit http://localhost:3000/ instead, or
                run `yarn run build` to test the production version.
                """,
                status=501,
            )

@csrf_exempt
def register_user(request):
    """
    Registers a user from the react frontend server.

    Request should contain patient and medication information.
    """

    request_data = request.POST
    print(request_data)

    patient_data = {
        'first_name': request_data['first_name'],
        'last_name': request_data['last_name'],
        'phone_number': request_data['phone_number'],
        'registration_date': timezone.now()
    }
	# check if patient is present in the database.
    if Patient.objects.filter(phone_number=patient_data['phone_number']).exists():
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

        _create_reminders(patient_data, medication_data, med_instance.id)

    return HttpResponse("OK")
    # save the data into the database

    # communicate with twillo

    # return the code to be used.


@csrf_exempt
def _sms_register(phone_num):
    # create client with credentials
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    # register user with phone_num
    validation_request = client.validation_requests \
        .create(
            friendly_name=phone_num,
            phone_number=phone_num
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


def reminder_message_helper(patient_name, medication_name):
    message = "Hi {0}! It's time to take your medications. \n{1}\nPlease give me an 'ok' once you've taken your pills!".format(
        patient_name, medication_name)
    return message


def _create_reminders(patient, medication, medication_id):
    # remind in 5 seconds
    now = datetime.datetime.now()
    scheduled_time = now + (datetime.timedelta(seconds=5))
    medication_name = medication['med_name'] + \
        " " + medication['dosage'] + medication['unit']

    message = reminder_message_helper(patient, medication_name)

    # create reminder
    reminder_data = {
        'scheduled_medication_time': scheduled_time,
    }

    reminder_instance = Reminder.objects.create(
        medication_id=medication_id,
        scheduled_medication_time=reminder_data['scheduled_medication_time'],
        completed=False
    )
    reminder_instance.save()

    # schedule task send_reminder
    send_reminder.schedule(args=(patient, reminder_instance.id, message,),
                           eta=scheduled_time)
    return


@csrf_exempt
def sms_response(request):
	request_data = request.POST
	message = request_data['Body']
	recipient_number = request_data['From']

	patient = list(Patient.objects.filter(phone_number=recipient_number))[0]
	print(patient)
	print(patient.id)
	# get all reminders linked to patient.
	medications = Medication.objects.filter(patient_id=patient.id)
	expired_reminders = []

	# get current time
	now = datetime.datetime.now()

	for med in medications:
		print(med)
		# get reminders
		reminders = Reminder.objects.filter(medication_id=medication.id)

		# check times
		for item in reminders:
			if item.scheduled_medication_time < now:
				# append to list if expired
				expired_reminders.append(item)
			
	# Cancel reminders
	for reminder in expired_reminders:
		reminder.completed = True
		reminder.time_responded = now
		reminder.save()

	message = "Thank you. Have a great day!"
	# set reminder to completed
	# and response time
	print(message)
	# create client with credentials
	client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
	# send message
	message = client.messages \
        .create(
            body=message,
            from_=ACCOUNT_NUMBER,
            to=recipient_number
        )
	return HttpResponse(str(message))
