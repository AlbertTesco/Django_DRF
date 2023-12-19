import os
from enum import Enum

import stripe


class PaymentMethod(str, Enum):
    """
    Класс enum с методом оплаты
    """
    CASH = 'Наличные'
    TRANSFER = 'Перевод на счет'


class PaymentService:
    """
    Класс для работы с платежами при помощи Stripe
    """
    stripe_secret_key = os.getenv('STRIPE_API_KEY')

    def __init__(self, stripe_secret_key):
        self.__stripe = stripe
        self.__stripe_secret_key = stripe_secret_key

    def create_payment(self, course: int, payment_sum: int, payment_method: PaymentMethod.TRANSFER):
        data = self.__stripe.PaymentIntent.create(
            object=course,
            amount=payment_sum,
            currency="usd",
            payment_method=payment_method,
            automatic_payment_methods={"enabled": True},
        )
        return data['id']
