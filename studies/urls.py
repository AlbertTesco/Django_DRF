from django.urls import path
from rest_framework.routers import DefaultRouter

from studies.api_views.course import CourseViewSet
from studies.api_views.lesson import *
from studies.apps import StudiesConfig

app_name = StudiesConfig.name

router = DefaultRouter()
router.register(r'courses', CourseViewSet, basename='сourse')

urlpatterns = [
                  path('lesson/create/', LessonCreateAPIView.as_view(), name='lesson-create'),
                  path('lesson/', LessonListAPIView.as_view(), name='lesson-list'),
                  path('lesson/detail/<int:pk>/', LessonRetrieveAPIView.as_view(), name='lesson-detail'),
                  path('lesson/update/<int:pk>/', LessonUpdateAPIView.as_view(), name='lesson-update'),
                  path('lesson/delete/<int:pk>/', LessonDestroyAPIView.as_view(), name='lesson-delete'),
              ] + router.urls
