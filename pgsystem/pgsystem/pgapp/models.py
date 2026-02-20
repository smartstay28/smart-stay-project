# pgapp/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('user', 'User'),
    )

    full_name = models.CharField(max_length=100)
    birth_date = models.DateField(null=True, blank=True)
    aadhar_number = models.CharField(max_length=20, unique=True)
    contact_number = models.CharField(max_length=15)
    occupation = models.CharField(max_length=50)
    address = models.TextField()
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

    def __str__(self):
        return self.username