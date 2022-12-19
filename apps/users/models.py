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


class Speciality(models.Model):
    speciality_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20, blank=True, null=True)
    code = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'speciality'


class Paramedic(models.Model):
    paramedic_id = models.IntegerField(primary_key=True)
    login = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    speciality = models.ForeignKey('Speciality', models.DO_NOTHING)
    medical_facility = models.ForeignKey('MedicalFacility', models.DO_NOTHING, blank=True, null=True)
    last_name = models.CharField(max_length=20, blank=True, null=True)
    first_name = models.CharField(max_length=20, blank=True, null=True)
    patronomic = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.last_name + ' ' + self.first_name + ' ' + self.patronomic

    class Meta:
        managed = False
        db_table = 'paramedic'


class MedicalFacility(models.Model):
    medical_facility_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'medical_facility'
