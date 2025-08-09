from django.shortcuts import render, reverse
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView
from .models import Device
from .forms import DeviceForm


class DeviceListView(ListView):
    template_name = "inventory/device_list.html"
    queryset = Device.objects.all()
    context_object_name = "devices"


class DeviceDetailView(DetailView):
    template_name = "inventory/device_detail.html"
    queryset = Device.objects.all()
    context_object_name = "device"


class DeviceCreateView(CreateView):
    template_name = "inventory/device_create.html"
    form_class = DeviceForm

    def get_success_url(self):
        return reverse("inventory:device_list")


class DeviceUpdateView(UpdateView):
    template_name = "inventory/device_update.html"
    queryset = Device.objects.all()
    form_class = DeviceForm

    def get_success_url(self):
        return reverse("inventory:device_list")
