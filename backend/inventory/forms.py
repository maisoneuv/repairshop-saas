from django import forms
from .models import Device, Category
from django.contrib.admin.widgets import FilteredSelectMultiple



class DeviceForm(forms.ModelForm):
    categories = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all(),
        widget=FilteredSelectMultiple("Categories", is_stacked=False),
        required=False
    )

    class Meta:
        model = Device
        fields = ["manufacturer", "model", "categories"]
