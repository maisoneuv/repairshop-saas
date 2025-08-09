from django.shortcuts import get_object_or_404, render, reverse
from .models import Customer, Asset
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView
from .forms import CustomerForm, CustomerAssetForm
from dal import autocomplete
from django.db.models import Q
from django.http import JsonResponse


from customers import models


class CustomerListView(ListView):
    template_name = "customers/customer_list.html"
    queryset = Customer.objects.all()
    context_object_name = "customers"


class CustomerDetailView(DetailView):
    template_name = "customers/customer_detail.html"
    queryset = Customer.objects.all()
    context_object_name = "customer"


class CustomerCreateView(CreateView):
    template_name = "customers/customer_create.html"
    form_class = CustomerForm

    def get_success_url(self):
        return reverse("customers:customer_list")


class CustomerUpdateView(UpdateView):
    template_name = "customers/customer_update.html"
    form_class = CustomerForm
    queryset = Customer.objects.all()

    def get_success_url(self):
        return reverse("customers:customer_list")


class CustomerAsetListView(ListView):
    template_name = "customers/asset_list.html"
    queryset = Asset.objects.all()
    context_object_name = "assets"


class CustomerAssetDetailView(DetailView):
    template_name = "customers/asset_detail.html"
    queryset = Asset.objects.all()
    context_object_name = "asset"


class CustomerAssetCreateView(CreateView):
    template_name = "customers/asset_create.html"
    form_class = CustomerAssetForm

    def get_success_url(self):
        return reverse("customers:asset_list")


class CustomerAssetUpdateView(UpdateView):
    template_name = "customers/asset_update.html"
    form_class = CustomerAssetForm
    queryset = Asset.objects.all()

    def get_success_url(self):
        return reverse("customers:asset_list")


class CustomerSearchView(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        print('bla:')
        if not self.request.user.is_authenticated:
            return Customer.objects.none()

        if not self.q:
            return Customer.objects.none()

        qs = Customer.objects.all()

        if self.q:
            qs = qs.filter(
                Q(phone_number__icontains=self.q) |
                Q(email__icontains=self.q)
            )
        return qs

    def get_result_label(self, customer):
        return f"{customer.full_name()} - {customer.phone_number} - {customer.email}"

    def get_selected_result_label(self, customer):
        return f"{customer.full_name()}"


def customer_phone_autocomplete(request):
    query = request.GET.get("q", "").strip()
    customers = Customer.objects.all()

    if query:
        customers = customers.filter(
            Q(phone_number__icontains=query)
        )
    else:
        customers = Customer.objects.none()

    results = [
        {"id": customer.id, "text": customer.phone_number}
        for customer in customers
    ]
    return JsonResponse(results, safe=False)


def customer_email_autocomplete(request):
    query = request.GET.get("q", "").strip()
    customers = Customer.objects.all()

    if query:
        customers = customers.filter(
            Q(email__icontains=query)
        )
    else:
        customers = Customer.objects.none()

    results = [
        {"id": customer.id, "text": f"{customer.full_name()} - {customer.email} - {customer.phone_number}"}
        for customer in customers
    ]
    return JsonResponse(results, safe=False)


def customer_name_autocomplete(request):
    query = request.GET.get("q", "").strip()
    customers = Customer.objects.all()

    if query:
        customers = customers.filter(
            Q(first_name__icontains=query) |
            Q(last_name__icontains=query) 
        )
    else:
        customers = Customer.objects.none()

    results = [
        {"id": customer.id, "text": f"{customer.full_name()} - {customer.email} - {customer.phone_number}"}
        for customer in customers
    ]
    return JsonResponse(results, safe=False)


def customer_details(request):
    customer_id = request.GET.get("id")
    
    if not customer_id:
        return JsonResponse({"success": False, "error": "No customer ID provided"}, status=400)

    customer = get_object_or_404(Customer, id=customer_id)
    name = customer.full_name()

    return JsonResponse({
        "success": True,
        "name": name,
        "email": customer.email,
        "phone": customer.phone_number
    })