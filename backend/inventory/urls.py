from django.urls import path
from .views import DeviceCreateView, DeviceDetailView, DeviceUpdateView, DeviceListView

app_name = "inventory"

urlpatterns = [
    path('all', DeviceListView.as_view(), name="device_list"),
    path('detail/<pk>/', DeviceDetailView.as_view(), name="device_detail"),
    path('detail/<pk>/update', DeviceUpdateView.as_view(), name="device_update"),
    path('create', DeviceCreateView.as_view(), name="device_create"),

]
