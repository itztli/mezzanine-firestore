from django.forms import ModelForm
from mezzanine_firestore.models import Patient

class Patient_Form(ModelForm):
     class Meta:
        model = Patient
        fields = ['firstName','lastName','gender','coutry','birtday']
