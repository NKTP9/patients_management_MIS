from django.db import models
from django.contrib.auth.models import AbstractUser

from datetime import date


class CustomUser(AbstractUser):
    birth_date = models.DateField('Дата рождения', default='2000-09-12')
    passport_series = models.CharField('Серия паспорта', max_length=4, default='')
    passport_number = models.CharField('Номер паспорта', max_length=6, default='')
    patronymic = models.CharField('Отчество', max_length=20, default='')
    phone = models.CharField('Телефон', max_length=11, default='')
    policy = models.CharField('Полис', max_length=16, default='')
    insurance_number = models.CharField('СНИЛС', max_length=13, default='')

    def __str__(self):
        return self.last_name + ' ' + self.first_name + ' ' + self.patronymic
