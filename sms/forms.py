from django.forms import ModelForm
from sms.models import Patient


class PatientForm(ModelForm):
    class Meta:
        model = PatientForm
