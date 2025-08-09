from django.urls import path
from .views import (CustomerListView,
                    CustomerCreateView,
                    CustomerUpdateView,
                    CustomerDetailView,
                    CustomerAsetListView,
                    CustomerAssetCreateView,
                    CustomerAssetDetailView,
                    CustomerAssetUpdateView,
                    CustomerSearchView, 
                    customer_details,
                    customer_phone_autocomplete,
                    customer_email_autocomplete,
                    customer_name_autocomplete)

app_name = "customers"

urlpatterns = [
    path('all', CustomerListView.as_view(), name="customer_list"),
    path('detail/<pk>/', CustomerDetailView.as_view(), name="customer_detail"),
    path('detail/<pk>/update', CustomerUpdateView.as_view(), name="customer_update"),
    path('create', CustomerCreateView.as_view(), name="customer_create"),
    path('assets', CustomerAsetListView.as_view(), name="asset_list"),
    path('asset/<pk>/', CustomerAssetDetailView.as_view(), name="asset_detail"),
    path('asset/<pk>/update', CustomerAssetUpdateView.as_view(), name="asset_update"),
    path('asset/create', CustomerAssetCreateView.as_view(), name="asset_create"),
    # path('customer-autocomplete/', CustomerSearchView.as_view(),name='customer-autocomplete'),
    path("api/customer-phone-autocomplete/", customer_phone_autocomplete, name="customer-phone-autocomplete"),
    path("api/customer-email-autocomplete/", customer_email_autocomplete, name="customer-email-autocomplete"),
    path("api/customer-name-autocomplete/", customer_name_autocomplete, name="customer-name-autocomplete"),
    path("api/customer-details/", customer_details, name="customer-details"),

]
