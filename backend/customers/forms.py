from django import forms
from .models import Customer, Asset


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ["first_name", "last_name", "email", "phone_number", "address"]


class CustomerAssetForm(forms.ModelForm):
    class Meta:
        model = Asset
        fields = ["serial_number", "customer", "device"]
