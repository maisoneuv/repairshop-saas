from _decimal import Decimal

from django.db import models
from customers.models import Customer, Asset
from service.models import Employee, Location
from core.models import Address
from django.core.validators import MinValueValidator


work_item_statuses = [
    ('New', 'New'),
    ('In Progress', 'In Progress'),
    ('Resolved', 'Resolved')
]

work_item_types = [
    ('Chargeable Repair', 'Chargeable Repair'),
    ('Warranty Repair', 'Warranty Repair')
]

priority_choices = [
    ('Express', 'Express'),
    ('Standard', 'Standard')
]

intake_methods = [
    ('Customer drop-off in person', 'Customer drop-off in person'),
    ('Shipped by customer', 'Shipped by customer'),
    ('Courier pickup from customer', 'Courier pickup from customer')
]

referral_sources = [
    ('Internet Search', 'Internet Search'),
    ('Social Media', 'Social Media'),
    ('Friend/Family Referral', 'Friend/Family Referral'),
    ('Online Advertisement', 'Online Advertisement'),
    ('Offline Advertisement', 'Offline Advertisement'),
    ('Walk-by', 'Walk-by'),
    ('Returning Customer', 'Returning Customer'),
    ('Other', 'Other')
]

payment_methods = [
    ('Card', 'Card'),
    ('Cash', 'Cash')
]


class WorkItem(models.Model):
    summary = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(choices=work_item_statuses, default='New')
    customer = models.ForeignKey(Customer, blank=False, null=False, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    closed_date = models.DateTimeField(blank=True, null=True)
    owner = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="owner") #todo
    due_date = models.DateField(null=True, blank=True)
    type = models.CharField(choices=work_item_types,default='Chargeable Repair')
    estimated_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True,
                                          validators=[MinValueValidator(Decimal('0.01'))])
    final_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True,
                                      validators=[MinValueValidator(Decimal('0.01'))])
    repair_cost = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True,
                                      validators=[MinValueValidator(Decimal('0.01'))])
    customer_dropoff_point = models.ForeignKey(Location, on_delete=models.CASCADE)
    customer_pickup_point = models.ForeignKey(Address, on_delete=models.CASCADE, null=True)
    customer_asset = models.ForeignKey(Asset, on_delete=models.CASCADE, blank=True, null=True)
    priority = models.CharField(choices=priority_choices, default='Standard')
    comments = models.TextField(blank=True, null=True)
    device_condition = models.TextField(blank=True, null=True)
    technician = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True, blank=True, related_name="technician")
    prepaid_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True,
                                         validators=[MinValueValidator(Decimal('0.01'))])
    intake_method = models.CharField(choices=intake_methods, default='Customer drop-off in person')
    referral_source = models.CharField(choices=referral_sources, blank=True, null=True)
    payment_method = models.CharField(choices=payment_methods, blank=True, null=True)
    # paid
    #currency todo

    def __str__(self):
        return self.summary


class Task(models.Model):
    summary = models.CharField(max_length=255, blank=False, null=False)
    description = models.TextField()
    work_item = models.ForeignKey(WorkItem, blank=True, null=True, on_delete=models.CASCADE, related_name="tasks")
    # status todo
    assigned_employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    due_date = models.DateField(null=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.summary


