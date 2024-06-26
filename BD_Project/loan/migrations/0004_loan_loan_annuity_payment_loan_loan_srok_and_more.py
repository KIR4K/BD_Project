# Generated by Django 4.2.11 on 2024-03-20 21:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('loan', '0003_payment'),
    ]

    operations = [
        migrations.AddField(
            model_name='loan',
            name='loan_annuity_payment',
            field=models.FloatField(blank=True, null=True, verbose_name='Аннуитетный платеж'),
        ),
        migrations.AddField(
            model_name='loan',
            name='loan_srok',
            field=models.IntegerField(default=1, verbose_name='Срок кредитования'),
        ),
        migrations.AddField(
            model_name='payment',
            name='penalty',
            field=models.IntegerField(default=0, verbose_name='Пеня'),
        ),
        migrations.AlterField(
            model_name='loan',
            name='loan_annual_interest',
            field=models.FloatField(verbose_name='Процентная ставка'),
        ),
        migrations.AlterField(
            model_name='loan',
            name='loan_sum',
            field=models.FloatField(verbose_name='Сумма кредита'),
        ),
        migrations.CreateModel(
            name='Payment_Plan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('loan', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='payment_plan', to='loan.loan')),
            ],
            options={
                'verbose_name': 'План',
                'verbose_name_plural': 'Планы',
            },
        ),
        migrations.AddField(
            model_name='payment',
            name='payment_plan',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='payments', to='loan.payment_plan'),
        ),
    ]
