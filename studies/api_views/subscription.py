from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from studies.models import Subscription
from studies.permissions import IsModerator, IsModerOrOwner
from studies.serializers import SubscriptionSerializer


class SubscriptionViewSet(APIView):
    permission_classes = [IsModerator, IsModerOrOwner]

    def post(self, request):
        request.data['subscribed'] = True
        serializer = SubscriptionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, user, course):
        try:
            subscription = Subscription.objects.get(user=user, course=course)
        except Subscription.DoesNotExist:
            return Response({'message': 'Подписка не найдена'}, status=status.HTTP_404_NOT_FOUND)

        subscription.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
