from django.db import models

from users.models import User

NULLABLE = {'blank': True, 'null': True}


class Course(models.Model):
    """Модель курса обучения"""
    title = models.CharField(max_length=200, verbose_name='Название')
    preview = models.ImageField(upload_to='course_previews/', verbose_name='Превью', **NULLABLE)
    description = models.TextField(verbose_name='Описание')
    owner = models.ForeignKey(User, related_name='owned_courses', verbose_name='Владелец', **NULLABLE,
                              on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'


class Lesson(models.Model):
    """Модель урока курса"""

    course = models.ForeignKey(Course, related_name='lesson', on_delete=models.CASCADE, **NULLABLE, verbose_name='Курс')

    name = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    preview = models.ImageField(upload_to='course_previews/', verbose_name='Превью', **NULLABLE)
    link_to_video = models.CharField(max_length=250, verbose_name='Ссылка на видео')
    owner = models.ForeignKey(User, related_name='owned_lessons', verbose_name='Владелец', **NULLABLE,
                              on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'
