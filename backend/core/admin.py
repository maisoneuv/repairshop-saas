from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _
from core import models
from customers.models import Customer, Asset
from tasks.models import WorkItem, Task
from inventory.models import Device, Category, InventoryItem, InventoryList, AttributeDefinition, PartAttributeValue
from service.models import Employee, Location


class UserAdmin(BaseUserAdmin):
    ordering = ['id']
    list_display = ['email', 'name', 'is_superuser', 'username']
    fieldsets = (
        (None, {'fields': ('email', 'name', 'password')}),
        (
            _('Permissions'),
            {
                'fields': (
                    'is_active',
                    'is_staff',
                    'is_superuser',
                )
            }
        ),
        (_('System Info'), {'fields': ('last_login',)})
    )
    readonly_fields = ['last_login']
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email',
                'username',
                'name',
                'password1',
                'password2',
                'is_active',
                'is_staff',
                'is_superuser',
            )
        }),
    )


@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ("manufacturer", "model",)
    filter_horizontal = ("categories",)


admin.site.register(models.User, UserAdmin)
admin.site.register(models.Address)
admin.site.register(Customer)
admin.site.register(Asset)
admin.site.register(WorkItem)
admin.site.register(Task)
admin.site.register(Employee)
admin.site.register(Location)
admin.site.register(Category)
admin.site.register(InventoryItem)
admin.site.register(InventoryList)
admin.site.register(AttributeDefinition)
admin.site.register(PartAttributeValue)
