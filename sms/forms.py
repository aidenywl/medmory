from django.forms import ModelForm
from sms.models import Patient, Medication, Reminder


class PatientForm(ModelForm):
    class Meta:
        model = PatientForm
            fields = ['first_name', 'last_name', 'phone_number', 'registration_date']
            
class MedicationForm(ModelForm):
    class Meta:
        model = MedicationForm
            fields = ['patient_id', 'med_name', 'dosage', 'unit', 'frequency', 'time_period']
            
class ReminderForm(ModelForm):
    class Meta:
        model = ReminderForm
            fields = ['medication_id', 'scheduled_medication_time', 'time_responded']
