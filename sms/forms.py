from django.forms import ModelForm
from sms.models import Patient, Medication, Reminder


class PatientForm(ModelForm):
    class Meta:
        model = Patient
        fields = ['first_name', 'last_name',
                  'phone_number']


class MedicationForm(ModelForm):
    class Meta:
        model = Medication
        fields = ['med_name', 'dosage',
                  'unit', 'frequency', 'time_period']


class ReminderForm(ModelForm):
    class Meta:
        model = Reminder
        fields = ['scheduled_medication_time', 'time_responded']
