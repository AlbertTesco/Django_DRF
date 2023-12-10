from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView

from studies.permissions import IsModerator, IsModerOrOwner
from users.models import User
from users.serializers import UserSerializer, MyTokenObtainPairSerializer


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


# class TokenRefreshView()

class UserViewSet(viewsets.ViewSet):

    def update(self, request, pk=None):
        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response({'message': 'Пользователь не найден'}, status=status.HTTP_404_NOT_FOUND)

        serializer = UserSerializer(user, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response({'message': 'Пользователь не найден'}, status=status.HTTP_404_NOT_FOUND)

        user.delete()
        return Response({'message': 'Пользователь успешно удален'}, status=status.HTTP_204_NO_CONTENT)
