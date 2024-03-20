from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver

class Client(models.Model):
    client_first_name = models.CharField('Имя', max_length=50)
    client_second_name = models.CharField('Фамилия', max_length=50)
    client_patronymic = models.CharField('Отчество', max_length=50)

    def __str__(self):
        return ' '.join(map(str,{self.client_second_name,self.client_first_name,self.client_patronymic}))

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

class Passport(models.Model):
    client = models.OneToOneField(Client, on_delete=models.CASCADE)
    passport_series = models.IntegerField('Серия паспорта')
    passport_number = models.IntegerField('Номер паспорта')
    passport_birth_date = models.DateField('Дата рождения')
    address = models.CharField('Адрес', max_length=255)  # Добавляем поле для адреса клиента
    region = models.CharField(max_length=100)
    oblast = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    house = models.CharField(max_length=10)
    building = models.CharField(max_length=10, blank=True, null=True)
    letter = models.CharField(max_length=1, blank=True, null=True)

    def save(self, *args, **kwargs):
        if self.client:
            # Разбиваем адрес на составляющие
            address_parts = str(self.address).split()

            # Устанавливаем значения для всех обязательных полей
            self.region = address_parts[0]
            self.oblast = address_parts[1]
            self.city = address_parts[2]
            self.street = address_parts[3]
            self.house = address_parts[4]

            # Устанавливаем значения для необязательных полей, если они присутствуют
            if len(address_parts) >= 6:
                self.building = address_parts[5]
            if len(address_parts) >= 7:
                self.letter = address_parts[6]

        super().save(*args, **kwargs)

    def __str__(self):
        return ' '.join(map(str,{self.passport_series,self.passport_number}))

    class Meta:
        verbose_name = 'Паспорт'
        verbose_name_plural = 'Паспорта'

'''@receiver(pre_save, sender=Client)
def ensure_client_has_passport(sender, instance, **kwargs):
    if not hasattr(instance, 'passport'):
        raise ValueError("Cannot save client without Passport")'''

'''@receiver(pre_save, sender=Passport)
def ensure_passport_has_client(sender, instance, **kwargs):
    if instance.client_id is None:
        raise ValueError("Cannot save Passport without client")'''