# Generated by Django 4.2.11 on 2024-03-17 16:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('loan_sum', models.IntegerField(verbose_name='Сумма кредита')),
                ('loan_annual_interest', models.IntegerField(verbose_name='Процентная ставка')),
                ('loan_balance', models.IntegerField(verbose_name='Баланс')),
                ('client', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='client.client')),
            ],
            options={
                'verbose_name': 'Кредит',
                'verbose_name_plural': 'Кредиты',
            },
        ),
    ]
