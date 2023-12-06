import random
from decimal import Decimal

from django.core.management import BaseCommand
from django.utils import timezone

from payment.models import Payment
from studies.models import Course, Lesson
from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        """Рандомное заполнение платежей для пользователей"""
        users = User.objects.all()
        courses = Course.objects.all()
        lessons = Lesson.objects.all()

        for item in users:
            payment = Payment(
                user=item,
                payment_date=timezone.now(),
                course=random.choice(courses) if courses else None,
                lesson=random.choice(lessons) if lessons else None,
                amount=Decimal(random.randrange(100, 50000)),
                payment_method=random.choice(['cash', 'transfer to account'])
            )

            payment.save()
