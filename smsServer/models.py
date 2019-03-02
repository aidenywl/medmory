

from django.db import models


class Patient(models.Model):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    registration_date = models.DateTimeField('patient registered')


class Medication(models.Model):
    med_name = models.CharField(max_length = 10)
    dosage = models.IntegerField(default=0)
    unit = models.CharField(max_length = 5)
    frequency = models.IntegerField(default=0)
