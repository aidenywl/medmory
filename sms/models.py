from django.db import models
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.


class Patient(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    phone_number = PhoneNumberField(blank=False, null=False)
    registration_date = models.DateTimeField(
        default=timezone.now, editable=False)


class Medication(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    med_name = models.CharField(max_length=10)
    dosage = models.IntegerField(default=0)
    unit = models.CharField(max_length=5)
    frequency = models.IntegerField(default=0)
    time_period = models.CharField(max_length=10)


class Reminder(models.Model):
    medication = models.ForeignKey(Medication, on_delete=models.DO_NOTHING)
    scheduled_medication_time = models.DateTimeField(blank=False, null=False)
    time_responded = models.DateTimeField(blank=True, null=True)
