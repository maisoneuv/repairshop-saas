from django import forms
from .models import WorkItem, Task
from dal import autocomplete
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, HTML, Div, Submit


class WorkItemForm(forms.ModelForm):
    class Meta:
        model = WorkItem
        fields = ["customer", "customer_asset", "description", "device_condition", "comments", "priority",
                  "intake_method",
                  "owner", "type", "customer_dropoff_point", "technician", "estimated_price", "prepaid_amount",
                  "referral_source",
                  "payment_method"]
        widgets = {
            'customer': autocomplete.ModelSelect2(url='customers:customer-autocomplete')
        }


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["summary", "description", "work_item", "assigned_employee", "due_date"]
        widgets = {
            "due_date": forms.SelectDateWidget()
        }
