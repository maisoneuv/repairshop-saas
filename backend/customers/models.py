from django.db import models
from django.core.validators import RegexValidator
from inventory.models import Device
from core.models import Address


class Customer(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255, blank=False, null=False)
    email = models.EmailField(unique=True, blank=False, null=False)
    address = models.OneToOneField(Address, on_delete=models.CASCADE, blank=True, null=True)

    phone_regex = RegexValidator(
        regex=r'\d{7,9}$',
        message='Phone number must be entered without any special characters. Up to 9 digits allowed'
    )

    phone_number = models.CharField(max_length=9, null=True, blank=True, validators=[phone_regex])

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name()


class Lead(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255, blank=False, null=False)
    email = models.EmailField(unique=True, blank=True, null=True)

    phone_regex = RegexValidator(
        regex=r'\d{7,9}$',
        message='Phone number must be entered without any special characters. Up to 9 digits allowed'
    )

    phone_number = models.CharField(max_length=9, null=True, blank=True, validators=[phone_regex])

    def full_name(self):
        return f"{self.first_name} {self.last_name}"


class Opportunity(models.Model):
    lead = models.ForeignKey(Lead, on_delete=models.SET_NULL, blank=True, null=True)
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    description = models.TextField(blank=False)


class Asset(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=False, blank=False)
    serial_number = models.CharField(max_length=255, null=False, blank=False)
    device = models.ForeignKey(Device, on_delete=models.CASCADE, related_name='assets', null=True)

    def __str__(self):
        return self.device.model
