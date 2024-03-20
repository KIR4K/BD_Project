from datetime import timedelta
from django.db import models
from client.models import Client as Client
from django.db.models.signals import post_save
from django.dispatch import receiver
from math import pow
from django.utils import timezone


class Loan(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    loan_sum = models.FloatField('Сумма кредита')
    loan_date = models.DateField('Дата', default=timezone.now)
    loan_annual_interest = models.FloatField('Процентная ставка', default=10)
    loan_balance = models.IntegerField('Баланс', default=0)
    loan_status = models.BooleanField('Статус кредита', default=False)
    loan_srok = models.IntegerField('Срок кредитования', default=1)  # Срок кредита в месяцах
    loan_annuity_payment = models.FloatField('Аннуитетный платеж', blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.pk:  # Проверяем, что объект новый
            # Расчет аннуитетного платежа
            monthly_interest_rate = self.loan_annual_interest / 100 / 12
            n = self.loan_srok
            annuity_payment = (self.loan_sum * monthly_interest_rate) / (1 - pow(1 + monthly_interest_rate, -n))
            self.loan_annuity_payment = annuity_payment
        super().save(*args, **kwargs)

    def __str__(self):
        return ' '.join(map(str, {self.loan_sum}))

    class Meta:
        verbose_name = 'Кредит'
        verbose_name_plural = 'Кредиты'


class Payment(models.Model):
    payment_plan = models.ForeignKey('Payment_Plan', on_delete=models.CASCADE, related_name='payments', null=True,
                                     blank=True)
    amount = models.IntegerField('Размер')
    date = models.DateTimeField('Дата')
    penalty = models.IntegerField('Пеня', default=0)

    def __str__(self):
        return f"Платеж {self.amount} от {self.date}"

    class Meta:
        verbose_name = 'Платёж'
        verbose_name_plural = 'Платежи'


class Payment_Plan(models.Model):
    loan = models.OneToOneField(Loan, on_delete=models.CASCADE, related_name='payment_plan')

    def __str__(self):
        return f"План платежей для кредита {self.loan}"

    class Meta:
        verbose_name = 'План'
        verbose_name_plural = 'Планы'


@receiver(post_save, sender=Loan)
def create_payment_plan(sender, instance, created, **kwargs):
    if created:
        # Создание объекта плана платежей
        payment_plan = Payment_Plan.objects.create(loan=instance)

        # Получение значения аннуитетного платежа из объекта кредита
        annuity_payment = instance.loan_annuity_payment

        # Инициализация текущей даты
        current_date = instance.loan_date

        # Создание платежей на основе аннуитетного платежа и текущей даты
        for _ in range(instance.loan_srok):
            Payment.objects.create(
                payment_plan=payment_plan,
                amount=annuity_payment,
                date=current_date
            )
            current_date += timedelta(days=30)  # Предполагая, что платежи делаются каждый месяц
