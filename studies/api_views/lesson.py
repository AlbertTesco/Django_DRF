from rest_framework import generics

from studies.models import Lesson
from studies.paginators import StudiesPaginator
from studies.permissions import IsModerator, IsModerOrOwner
from studies.serializers import LessonSerializer


class LessonCreateAPIView(generics.CreateAPIView):
    """Create a Lesson"""
    permission_classes = [IsModerator]
    serializer_class = LessonSerializer


class LessonListAPIView(generics.ListAPIView):
    """List a Lesson"""
    permission_classes = [IsModerator, IsModerOrOwner]
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    pagination_class = StudiesPaginator


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    """Retrieve a Lesson"""
    permission_classes = [IsModerator, IsModerOrOwner]
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonUpdateAPIView(generics.UpdateAPIView):
    """Update a Lesson"""
    permission_classes = [IsModerator, IsModerOrOwner]
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonDestroyAPIView(generics.DestroyAPIView):
    """Delete a Lesson"""
    permission_classes = [IsModerator, IsModerOrOwner]
    queryset = Lesson.objects.all()
