from rest_framework import serializers
from .models import Customer, UnitCharge, MeterReading
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


class MeterReadingSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeterReading
        fields = ["customer", "previous_reading", "meter_reading", "consumption"]
