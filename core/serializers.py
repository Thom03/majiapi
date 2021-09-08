from rest_framework import serializers
from .models import Customer, UnitCharge, MeterReading, PumpedUnits
from django.contrib.auth.models import User


class CustomerSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Customer
        fields = ['owner', 'first_name', 'middle_name', 'last_name', 'national_id', 'phone_number', 'email']


class UserSerializer(serializers.ModelSerializer):
    customers = serializers.PrimaryKeyRelatedField(many=True, queryset=Customer.objects.all())

    class Meta:
        fields = ['id', 'username', 'customers']


class UnitChargeSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnitCharge
        fields = ['user', 'charge', ]

# TODO: Refactoring this code to run as an app
class MeterReadingSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeterReading
        fields = ["customer", "previous_reading", "meter_reading", "consumption"]
        read_only_fields = ("previous_reading",)

    def validate(self, attrs):
        customer = attrs.get("customer")
        user = self.context['view'].request.user
        latest_customer_reading = MeterReading.objects.filter(customer=customer, customer__owner=user).first()
        if latest_customer_reading:
            if not attrs["meter_reading"] > latest_customer_reading.meter_reading:
                raise serializers.ValidationError(
                    f"Current meter reading cannot be less than {latest_customer_reading.meter_reading}."
                )
        return attrs

# TODO: Refactoring this code to run as an app
class PumpedUnitsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PumpedUnits
        fields = ["user", "yesterday_reading", "meter_reading", "units_pumped"]
        read_only_fields = ("yesterday_reading",)

    def validate(self, attrs):
        user = attrs.get("auth.User")
        user = self.context['view'].request.user
        latest_pumped_reading = PumpedUnits.objects.filter(user=user).first()
        if latest_pumped_reading:
            if not attrs["meter_reading"] > latest_pumped_reading.meter_reading:
                raise serializers.ValidationError(
                    f"Current meter reading cannot be less than {latest_pumped_reading.meter_reading}."
                )
        return attrs

