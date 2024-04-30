from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api import AppViewSet

router = DefaultRouter()
router.register(r'app', AppViewSet, basename='app')

urlpatterns = [
    path('api/', include(router.urls)),
]
