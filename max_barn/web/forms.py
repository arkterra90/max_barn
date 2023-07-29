from django.forms import ModelForm
from .models import *

class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = "__all__"

class BuildingForm(ModelForm):
    class Meta:
        model = Building
        fields = "__all__"