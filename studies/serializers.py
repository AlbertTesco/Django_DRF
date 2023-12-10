from rest_framework import serializers

from studies.models import Lesson, Course


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ('id', 'name', 'description', 'course', 'link_to_video', 'preview', 'owner',)

    def create(self, validated_data):
        user = self.context['request'].user  # Получение пользователя из запроса
        course = Lesson.objects.create(owner=user, **validated_data)
        return course


class CourseSerializer(serializers.ModelSerializer):
    lessons_count = serializers.SerializerMethodField()
    lesson = LessonSerializer(many=True)

    class Meta:
        model = Course
        fields = ('id', 'title', 'preview', 'description', 'lessons_count', 'lesson', 'owner')

    def get_lessons_count(self, obj):
        return obj.lesson.count()

    def create(self, validated_data):
        user = self.context['request'].user  # Получение пользователя из запроса
        lesson = Course.objects.create(owner=user, **validated_data)
        return lesson
