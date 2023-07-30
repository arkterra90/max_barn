from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


STATE_CHOICES = (
    ('AR', 'Arkansas'),
    ('MO', 'Missouri'),
    ('OK', 'Oklahoma'),
)

COLOR_CHOICES = [
        ('White', 'White'),
        ('Black', 'Black'),
        ('Light Gray', 'Light Gray'),
        ('Gray', 'Gray'),
        ('Dark Gray', 'Dark Gray'),
        ('Red', 'Red'),
        ('Maroon', 'Maroon'),
        ('Yellow', 'Yellow'),
        ('Green', 'Green'),
        ('Blue', 'Blue'),
        ('Purple', 'Purple'),
        ('Pink', 'Pink'),
    ]

BARN_TYPE = [
    ('House', 'House'),
    ('Personal Shop', 'Personal Shop'),
    ('Barn', 'Barn'),
    ('Shed', 'Shed'),
    ('Commercial Building', 'Commercial Building'),
    ('Garage', 'Garage')
]

CUST_STATUS = [
    ('Price Shopping', 'Price Shopping'),
    ('Ready To Build', 'Ready To Build'),
    ('Future Build', 'Future Build')
]

class User(AbstractUser):
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='web_users',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups',
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='web_users',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

class Customer(models.Model):

    name_first = models.CharField(max_length=64, verbose_name="First Name")
    name_last = models.CharField(max_length=64, verbose_name="Last Name")
    address = models.CharField(max_length=200)
    add_city = models.CharField(max_length=64, verbose_name="City")
    add_state = models.CharField(max_length=2, choices=STATE_CHOICES, verbose_name="State")
    zip = models.CharField(max_length=12, null=True, blank=True)
    phone_number = models.CharField(max_length=16, verbose_name="Phone Number")
    email = models.EmailField()
    date = models.DateTimeField(default=timezone.now)
    notes = models.TextField(blank=True, null=True)
    barn_type = models.CharField(max_length=20, choices=BARN_TYPE, verbose_name="Desired Structure Usuage", null=True, blank=True)


    def __str__(self):
        return f"{self.name_first} {self.name_last} {self.address} {self.add_city} {self.add_state} {self.phone_number} {self.email} {self.date}"
    
class Contact(models.Model):

    cust = models.ForeignKey(Customer, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=CUST_STATUS)
    possible_build_date = models.DateTimeField()
    site_details = models.TextField(verbose_name="Site Details")
    on_site_appointment = models.DateTimeField()
    made_contact = models.BooleanField(default=False)
    notes = models.TextField()

    def __str__(self):
        return f"{self.cust} {self.status} {self.possible_build_date} {self.site_details} {self.on_site_appointment} {self.notes}"
    

class Building(models.Model):
    cust = models.ForeignKey(Customer, on_delete=models.CASCADE)
    width = models.IntegerField()
    length = models.IntegerField()
    height = models.IntegerField()
    concrete = models.BooleanField(default=False)
    color = models.CharField(max_length=12, choices=COLOR_CHOICES)
    trim = models.CharField(max_length=20, choices=COLOR_CHOICES)
    porch = models.BooleanField(default=False)
    porch_concrete = models.BooleanField(default=False)
    porch_length = models.IntegerField(verbose_name="Porch Length", null=True, blank=True)
    porch_width = models.IntegerField(verbose_name="Porch Width", null=True, blank=True)
    windows = models.IntegerField(null=True, blank=True, verbose_name="Quantity of Windows")
    walk_doors = models.IntegerField(null=True, blank=True, verbose_name="Quantity of Walkin Doors")
    over_head_doors = models.IntegerField(null=True, blank=True, verbose_name="Quantity of Over Head Doors")
    over_head_height = models.IntegerField(null=True, blank=True, verbose_name="Over Head Door Height")
    over_head_width = models.IntegerField(null=True, blank=True, verbose_name="Over Head Door Width")
    plumbing = models.BooleanField(default=False)
    cust_use = models.TextField(null=True, blank=True, verbose_name="Customer Use Case:")
    notes = models.TextField(null=True, blank=True)
    

    def __str__(self):
        return f"{self.cust} {self.width} {self.length} {self.height} {self.concrete} {self.color} {self.trim} {self.porch} {self.porch_concrete} {self.porch_length} {self.porch_width} {self.windows} {self.walk_doors} {self.over_head_doors} {self.over_head_height} {self.over_head_width} {self.plumbing} {self.cust_use} {self.notes}"

class Payment(models.Model):
    project = models.ForeignKey(Building, on_delete=models.CASCADE)
    first_pay = models.BooleanField(default=False, blank=True, null=True)
    first_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    first_date = models.DateTimeField(blank=True, null=True)
    final_pay = models.BooleanField(default=False, blank=True, null=True)
    final_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)