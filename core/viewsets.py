from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework import viewsets, permissions, generics
from core.models import Customer
from core.serializers import CustomerSerializer, UserSerializer
from core.permissions import IsOwnerOrReadOnly
from django.contrib.auth.models import User


# Create your views here.


class CustomerViewSet(viewsets.ModelViewSet):
    """
        This viewset automatically provides `list`, `create`, `retrieve`,
        `update` and `destroy` actions."""

    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [IsAuthenticated, ]

    def get_queryset(self):
        current_user = self.queryset.filter(owner=self.request.user)
        return current_user

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class UserViewset(viewsets.ReadOnlyModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = User.objects.all()
    serializer_class = UserSerializer
