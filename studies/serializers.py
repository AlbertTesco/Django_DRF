from rest_framework import serializers

from studies.models import Lesson, Course, Subscription
from studies.validators import LessonCustomValidator


class LessonSerializer(serializers.ModelSerializer):
    """Lesson model serializer"""

    class Meta:
        model = Lesson
        fields = ('id', 'name', 'description', 'course', 'link_to_video', 'preview', 'owner',)
        validators = [LessonCustomValidator(field='link_to_video')]

    def create(self, validated_data):
        user = self.context['request'].user  # Получение пользователя из запроса
        course = Lesson.objects.create(owner=user, **validated_data)
        return course


class CourseSerializer(serializers.ModelSerializer):
    """Course model serializer"""

    lessons_count = serializers.SerializerMethodField()
    lessons = LessonSerializer(source='lesson', many=True, read_only=True)
    is_subscribed = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = ('id', 'title', 'preview', 'description', 'lessons_count', 'lessons', 'owner', 'is_subscribed')

    def get_lessons_count(self, obj):
        return obj.lesson.count()

    def get_is_subscribed(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            try:
                Subscription.objects.get(user=user, course=obj)
                return True
            except Subscription.DoesNotExist:
                return False
        return False

    def create(self, validated_data):
        user = self.context['request'].user  # Получение пользователя из запроса
        lesson = Course.objects.create(owner=user, **validated_data)
        return lesson


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = ('id', 'user', 'course', 'subscribed',)
