from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail


@shared_task
def send_update_info(email):
    send_mail(
        subject='Курс обновлен',
        message='Курс был обновлен, проверьте новые материалы',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[email]
    )
