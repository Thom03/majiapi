from django.urls import path, include
from rest_framework.routers import DefaultRouter

from core.urls import api_urlpatterns as core_urls

app_name = 'api'

router = DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('core/', include(core_urls)),
    # path('auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('auth/', include('rest_auth.urls'))
]
