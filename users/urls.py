from django.urls import path
from rest_framework.routers import DefaultRouter

from users.api_views.user import UserViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
urlpatterns = [

              ] + router.urls
