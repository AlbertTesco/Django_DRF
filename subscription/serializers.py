from rest_framework import serializers

from subscription.models import Subscription


class SubscriptionSerializers(serializers.ModelSerializer):
    """Serializer for subscription model"""

    class Meta:
        model = Subscription
        fields = ('id', 'course',)
