from django.contrib import admin
from core.models import Customer, UnitCharge, MeterReading, Billing, PumpedUnits


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


@admin.register(Billing)
class BillingAdmin(admin.ModelAdmin):
    list_display = (
        "customer",
        "status",
        "created",
    )

    list_filter = (
        "customer",
       
    )

@admin.register(PumpedUnits)
class PumpedUnitsAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "meter_reading",
        "yesterday_reading",
        "units_pumped",
        "created",
    )

    list_filter = (
        "created",
        "user",
    )


# admin.site.register(Customer)
