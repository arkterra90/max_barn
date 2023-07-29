from django.db import models
from django.contrib.auth.models import AbstractUser


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
    add_state = models.CharField(max_length=2, choices=STATE_CHOICES, unique=True, verbose_name="State")
    phone_number = models.CharField(max_length=16, verbose_name="Phone Number")
    email = models.EmailField()

    def __str__(self):
        return f"{self.name_first} {self.name_last} {self.address} {self.add_city} {self.add_state} {self.phone_number} {self.email}"
    

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
    windows = models.IntegerField(null=True, blank=True)
    walk_doors = models.IntegerField(null=True, blank=True)
    over_head_doors = models.IntegerField(null=True, blank=True)
    over_head_height = models.IntegerField(null=True, blank=True)
    over_head_width = models.IntegerField(null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    plumbing = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.cust.name_first} {self.cust.name_last} | {self.width}x{self.length}x{self.height} | Concrete: {'Yes' if self.concrete else 'No'} | Color: {self.color} | Trim: {self.trim} | Porch: {'Yes' if self.porch else 'No'} | Porch Concrete: {'Yes' if self.porch_concrete else 'No'} | Porch Size: {self.porch_length}x{self.porch_width} | Windows: {self.windows} | Walk Doors: {self.walk_doors} | Overhead Doors: {self.over_head_doors} | Overhead Size: {self.over_head_height}x{self.over_head_width} | Plumbing: {'Yes' if self.plumbing else 'No'}"

