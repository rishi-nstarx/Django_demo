from django import forms
from .models import PersonalInfo

class PersonalInfoForm(forms.Form):
    personal_info = forms.ModelChoiceField(queryset=PersonalInfo.objects.all(), label="select individual's info")
    
