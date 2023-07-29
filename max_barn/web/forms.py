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