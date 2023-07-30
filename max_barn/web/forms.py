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

class CustomerNoteForm(ModelForm):
    class Meta:
        model = CustomerNote
        exclude = ['cust_note_date', 'cust']

class BuildingNoteForm(ModelForm):
    class Meta:
        model = BuildingNote
        exclude = ['building', 'build_note_date']

class PaymentForm(ModelForm):
    class Meta:
        model = Payment
        fields = "__all__"