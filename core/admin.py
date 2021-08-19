from django.contrib import admin
from core.models import Customer, UnitCharge, MeterReading


# Register your models here.

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "owner",
        "national_id",
        "first_name",
        "middle_name",
        "last_name",
        "phone_number"
    )

    list_filter = (
        "created",
    )


@admin.register(UnitCharge)
class UnitChargeAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "charge",

    )


@admin.register(MeterReading)
class MeterReadingAdmin(admin.ModelAdmin):
    list_display = (
        "customer",
        "meter_reading",
        "previous_reading",
        "consumption",
        "created",
    )

    list_filter = (
        "created",
        "customer",
    )

# admin.site.register(Customer)
