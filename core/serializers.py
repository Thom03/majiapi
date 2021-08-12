from rest_framework import serializers
from .models import Customer
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
