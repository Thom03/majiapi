from django.urls import path, include
from rest_framework.routers import DefaultRouter

from core.viewsets import CustomerViewSet, UserViewset

app_name = 'core'

# Registering routes
router = DefaultRouter()
router.register('customers', CustomerViewSet)
router.register('users', UserViewset)

api_urlpatterns = [
    path('', include(router.urls))
]

urlpatterns = [

]