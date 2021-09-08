from django.db import models

# Create your models here.
from django.utils.translation import ugettext_lazy as _


# Create your models here.
class Customer(models.Model):
    owner = models.ForeignKey('auth.User', related_name='customers', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now=True)
    first_name = models.CharField(max_length=100, blank=True)
    middle_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    national_id = models.IntegerField(unique=True)
    phone_number = models.CharField(max_length=13, blank=True)
    email = models.EmailField()

    class Meta:
        ordering = ['created']
        db_table = 'customers'
        verbose_name = _("Customer")
        verbose_name_plural = _("Customers")

    def __str__(self):
        return self.first_name


class UnitCharge(models.Model):
    user = models.OneToOneField('auth.User', related_name='unitcharge', on_delete=models.CASCADE, primary_key=True)
    created = models.DateTimeField(auto_now=True)
    charge = models.FloatField(max_length=100, blank=True)

    class Meta:
        verbose_name = _("UnitCharge")
        verbose_name_plural = _("UnitCharges")


class MeterReading(models.Model):
    customer = models.ForeignKey('core.Customer', related_name='meterreading', on_delete=models.CASCADE)
    meter_reading = models.FloatField(max_length=14, blank=True)
    created = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created', ]
        get_latest_by = ("created",)

    @property
    def previous_reading(self):
        existing = MeterReading.objects.filter(customer=self.customer, created__lt=self.created).first()
        if existing:
            return existing.meter_reading
        return 0

    @property
    def consumption(self):
        # if self.meter_reading is not None:
        # previous_reading = MeterReading.objects.latest().meter_reading
        consumption = self.meter_reading - self.previous_reading
        return consumption
# TODO: Calculation of amount
class Billing(models.Model):
    STATUS_PENDING, STATUS_PAID = ("PENDING", "PAID", )
    customer = models.ForeignKey('core.Customer', related_name='billing', on_delete=models.CASCADE)
    status = models.CharField(
        max_length=10,
        choices=(
            (STATUS_PENDING, STATUS_PENDING),
            (STATUS_PAID, STATUS_PAID)
        ),
        default=STATUS_PENDING
    )
    created = models.DateTimeField(auto_now=True)

    # @property
    # def amount(self):
    #     amount = UnitCharge.charge. * MeterReading.objects.latest().consumption
    #     return amount

class PumpedUnits(models.Model):
    user = models.ForeignKey('auth.User', related_name='pumpedunits', on_delete=models.CASCADE)
    meter_reading = models.FloatField(max_length=14, blank=True)
    created = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created', ]
        get_latest_by = ("created",)

    @property
    def yesterday_reading(self):
        existing = PumpedUnits.objects.filter(user=self.user, created__lt=self.created).first()
        if existing:
            return existing.meter_reading
        return 0

    @property
    def units_pumped(self):
        # if self.meter_reading is not None:
        # previous_reading = MeterReading.objects.latest().meter_reading
        units_pumped = self.meter_reading - self.yesterday_reading
        return units_pumped

   


