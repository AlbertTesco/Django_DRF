from rest_framework import viewsets
from studies.models import Course
from studies.permissions import IsModerator, IsModerOrOwner
from studies.serializers import CourseSerializer


class CourseViewSet(viewsets.ModelViewSet):
    """ A viewset that provides default `create()`, `retrieve()`, `update()`,
    `partial_update()`, `destroy()` and `list()` actions."""

    permission_classes = [IsModerator, IsModerOrOwner]
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
