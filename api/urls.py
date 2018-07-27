# api/urls.py
from django.urls import path

from .views import UserViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('users', UserViewSet, base_name='Users')
urlpatterns = router.urls