import datetime
from django.utils import timezone
from users.models import User


def disable_users():
    """Periodic task to disconnect inactive users"""
    print('Запущена задача деактивации пользователей')

    disable_period = datetime.datetime.now(timezone.utc) - datetime.timedelta(days=30)
    users_for_disable = User.objects.filter(last_login__lte=disable_period, is_active=True)
    users_for_disable.update(is_active=False)
