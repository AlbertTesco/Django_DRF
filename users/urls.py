from django.urls import path
from rest_framework.routers import DefaultRouter

from users.api_views.user import UserViewSet, MyTokenObtainPairView
from users.apps import UsersConfig

app_name = UsersConfig.name

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')

urlpatterns = [
                  path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
                  # path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
              ] + router.urls
