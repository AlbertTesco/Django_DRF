from rest_framework.generics import CreateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated
from subscription.serializers import SubscriptionSerializers

from subscription.models import Subscription


class SubscriptionCreateAPIView(CreateAPIView):
    """
    Контроллер для создания подписки
    """
    serializer_class = SubscriptionSerializers
    permission_classes = [IsAuthenticated]


class SubscriptionDeleteAPIView(DestroyAPIView):
    """
    Контроллер для удаления подписки
    """
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializers
    permission_classes = [IsAuthenticated]
