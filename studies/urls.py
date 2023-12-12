from django.urls import path
from rest_framework.routers import DefaultRouter

from studies.api_views.course import CourseViewSet
from studies.api_views.lesson import *
from studies.api_views.subscription import SubscriptionViewSet
from studies.apps import StudiesConfig

app_name = StudiesConfig.name

router = DefaultRouter()
router.register(r'courses', CourseViewSet, basename='сourse')

urlpatterns = [
                  path('lesson/', LessonListAPIView.as_view(), name='lesson-list'),
                  path('lesson/create/', LessonCreateAPIView.as_view(), name='lesson-create'),
                  path('lesson/update/<int:pk>/', LessonUpdateAPIView.as_view(), name='lesson-update'),
                  path('lesson/delete/<int:pk>/', LessonDestroyAPIView.as_view(), name='lesson-delete'),
                  path('lesson/detail/<int:pk>/', LessonRetrieveAPIView.as_view(), name='lesson-detail'),

                  # Маршруты для создания и удаления подписок
                  path('subscriptions/', SubscriptionViewSet.as_view(), name='subscription-create'),
                  path('subscriptions/<int:user>/<int:course>/', SubscriptionViewSet.as_view(),
                       name='subscription-delete'),
              ] + router.urls
