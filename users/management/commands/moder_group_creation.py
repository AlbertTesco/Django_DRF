from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.core.management import BaseCommand

from studies.models import Lesson, Course


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        moderator_group, created = Group.objects.get_or_create(name='Модераторы')

        lesson_content_type = ContentType.objects.get_for_model(Lesson)
        course_content_type = ContentType.objects.get_for_model(Course)

        view_lesson_permission = Permission.objects.get(content_type=lesson_content_type, codename='view_lesson')
        change_lesson_permission = Permission.objects.get(content_type=lesson_content_type, codename='change_lesson')
        view_course_permission = Permission.objects.get(content_type=course_content_type, codename='view_course')
        change_course_permission = Permission.objects.get(content_type=course_content_type, codename='change_course')

        moderator_group.permissions.add(view_lesson_permission, change_lesson_permission,
                                        view_course_permission, change_course_permission)
