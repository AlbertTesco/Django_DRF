from django.db import models

from studies.models import Course
from users.models import User


class Subscription(models.Model):
    """
    Модель подписки
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Владелец подписки', null=True,
                             related_name='users')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Подписка на курс',
                               related_name='courses')
    is_active = models.BooleanField(default=True, verbose_name='Состояние подписки')

    def __str__(self):
        """
        Возвращение строкового представления объекта
        """
        return f'{self.user} - {self.well}'

    class Meta:
        """
        Настройки для наименования объекта/объектов
        """
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'
