from django.urls import path, include
from rest_framework.routers import DefaultRouter

from core.viewsets import CustomerViewSet, UserViewset, UnitchargeViewset, MeterReadingViewset, PumpedUnitViewset

app_name = 'core'

# Registering routes
router = DefaultRouter()
router.register('customers', CustomerViewSet)
router.register('users', UserViewset)
router.register('unitcharge', UnitchargeViewset)
router.register('meterreading', MeterReadingViewset)
router.register('pumpedunits', PumpedUnitViewset)

api_urlpatterns = [
    path('', include(router.urls))
]

urlpatterns = [

]