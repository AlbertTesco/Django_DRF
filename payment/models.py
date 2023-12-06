from django.db import models

from studies.models import Course, Lesson
from users.models import User

# Create your models here.
NULLABLE = {'blank': True, 'null': True}


class Payment(models.Model):
    PAYMENT_METHOD_CHOICES = [
        ('cash', 'Наличные'),
        ('bank_transfer', 'Перевод на счет'),
    ]

    user = models.ForeignKey(User, on_delete=models.SET_NULL, verbose_name='Пользователь', **NULLABLE,
                             related_name='payment')
    payment_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата оплаты')
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, verbose_name='Курс', **NULLABLE,
                               related_name='payment')
    lesson = models.ForeignKey(Lesson, on_delete=models.SET_NULL, verbose_name='Урок', **NULLABLE,
                               related_name='payment')
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Сумма оплаты')
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHOD_CHOICES, verbose_name='Способ оплаты')

    def __str__(self):
        return f"Payment for {self.course} or {self.lesson} by {self.user.username}"

    class Meta:
        verbose_name = 'Платеж'
        verbose_name_plural = 'Платежи'

