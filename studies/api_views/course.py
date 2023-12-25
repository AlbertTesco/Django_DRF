from rest_framework import viewsets
from rest_framework.response import Response

from studies.models import Course, Subscription
from studies.paginators import StudiesPaginator
from studies.permissions import IsModerator, IsModerOrOwner
from studies.serializers import CourseSerializer
from studies.tasks import send_update_info


class CourseViewSet(viewsets.ModelViewSet):
    """ A viewset that provides default `create()`, `retrieve()`, `update()`,
    `partial_update()`, `destroy()` and `list()` actions."""

    permission_classes = [IsModerator, IsModerOrOwner]
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    pagination_class = StudiesPaginator

    def perform_update(self, serializer):
        """
        Метод для обновления курса
        """
        serializer.save()
        pk = self.kwargs.get('pk')
        course = Course.objects.get(pk=pk)
        subscription = Subscription.objects.filter(course=course, is_active=True)
        emails = list(subscription.values_list('user__email', flat=True))

        send_update_info.delay(emails)
        return Response('Messages sent.')
