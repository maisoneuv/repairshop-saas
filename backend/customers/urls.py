from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (CustomerListView,
                    CustomerCreateView,
                    CustomerUpdateView,
                    CustomerDetailView,
                    CustomerAsetListView,
                    CustomerAssetCreateView,
                    CustomerAssetDetailView,
                    CustomerAssetUpdateView,
                    CustomerSearchView,
                    CustomerPhoneSearchView,
                    customer_search,
                    select_customer,
                    load_new_customer_fields,
                    customer_create_inline,
                    asset_create_inline,
                    get_customer_assets,
                    CustomerAPISearchView,
                    get_referral_sources,
                    CustomerViewSet)

app_name = "customers"

router = DefaultRouter()
router.register(r'customers', CustomerViewSet, basename="customer")

urlpatterns = [
    path('all', CustomerListView.as_view(), name="customer_list"),
    path('detail/<pk>/', CustomerDetailView.as_view(), name="customer_detail"),
    path('detail/<pk>/update', CustomerUpdateView.as_view(), name="customer_update"),
    path('create', CustomerCreateView.as_view(), name="customer_create"),
    path('assets', CustomerAsetListView.as_view(), name="asset_list"),
    path('asset/<pk>/', CustomerAssetDetailView.as_view(), name="asset_detail"),
    path('asset/<pk>/update', CustomerAssetUpdateView.as_view(), name="asset_update"),
    path('asset/create', CustomerAssetCreateView.as_view(), name="asset_create"),
    path('customer-autocomplete/', CustomerSearchView.as_view(),name='customer_autocomplete'),
    path('customer-phone-autocomplete/', CustomerPhoneSearchView.as_view(),name='customer_phone_autocomplete'),
    path('customer-search/', customer_search,name='customer_search'),
    path('select-customer/<pk>/', select_customer, name='select_customer'),
    path('load-new-customer-fields/', load_new_customer_fields, name='load_new_customer_fields'),
    path('create-inline/', customer_create_inline, name='customer_create_inline'),
    path('asset-create-inline/', asset_create_inline, name='asset_create_inline'),
    path('customer-assets/<int:pk>/', get_customer_assets, name='customer_assets'),
    path('api/customers/search/', CustomerAPISearchView.as_view(), name='customer-api-search'),
    # path('api/customers/', CustomerCreateListView.as_view(), name='customer-list-create'),
    path('api/referral-sources/', get_referral_sources, name='referral-sources'),
    path("api/", include(router.urls)),


]
