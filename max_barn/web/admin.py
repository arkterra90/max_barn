from django.contrib import admin
from .models import *


admin.site.register(Customer)
admin.site.register(Building)
admin.site.register(Payment)
admin.site.register(Contact)
admin.site.register(CustomerNote)
admin.site.register(BuildingNote)

# Register your models here.
