from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    MEMBERSHIP_STATUS_CHOICES = [
        ("N", "New"),
        ("LIF", "Lifetime"),
        ("LAP", "Lapsed"),
        ("X", "X"),
        ("OFF", "Off"),
        ("F", "F"),
    ]

    membership_number = models.CharField(max_length=255, unique=True, blank=True)
    membership_status = models.CharField(
        max_length=4, choices=MEMBERSHIP_STATUS_CHOICES, blank=True
    )
    
    title = models.CharField(max_length=255, blank=True)
    forename = models.CharField(max_length=255, blank=True)
    surname = models.CharField(max_length=255, blank=True)
    initial = models.CharField(max_length=255, blank=True)
    address_line1 = models.CharField(max_length=255, blank=True)
    address_line2 = models.CharField(max_length=255, blank=True)
    address_line3 = models.CharField(max_length=255, blank=True)
    town = models.CharField(max_length=255, blank=True)
    country = models.CharField(max_length=255, blank=True)
    postcode = models.CharField(max_length=255, blank=True)
    telephone_number = models.CharField(max_length=255, blank=True)
    email_address = models.EmailField(blank=True)
    notes = models.TextField(blank=True)
    last_payment_received_date = models.DateField(null=True, blank=True)
    annual_subscription = models.CharField(max_length=255, blank=True)
    paid_to_lbm_issue = models.CharField(max_length=255, blank=True)
    pay_subs_to = models.CharField(max_length=255, blank=True)
    outstanding_giro_letter_number = models.CharField(max_length=255, blank=True)
    spare = models.TextField(blank=True)
    
