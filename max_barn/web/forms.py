from django.forms import ModelForm
from .models import *

class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        exclude = ['date', 'notes']

class BuildingForm(ModelForm):
    class Meta:
        model = Building
        fields = "__all__"

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        exclude = ['cust', 'possible_build_date', 'on_site_appointment']