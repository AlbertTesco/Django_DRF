from rest_framework.routers import DefaultRouter

from payment.api_views.payment import PaymentViewSet
from payment.apps import PaymentConfig

app_name = PaymentConfig.name

router = DefaultRouter()
router.register(r'payment', PaymentViewSet, basename='payment')

urlpatterns = [

              ] + router.urls
