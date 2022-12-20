from django import forms
from django.contrib.auth.models import Group
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from apps.users.models import CustomUser, Paramedic


class CustomUserCreationForm(UserCreationForm):
    # groups = forms.ModelChoiceField(queryset=Group.objects.all())
    groups = forms.ModelChoiceField(queryset=Group.objects.exclude(name='Администратор'))

    class Meta:
        model = CustomUser
        # fields = "__all__"
        fields = ('username', 'email', 'first_name', 'last_name', 'passport_number',
                  'passport_series', 'patronymic', 'phone', 'policy', 'insurance_number')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        # fields = "__all__"
        fields = ('username', 'email', 'first_name', 'last_name', 'passport_number',
                  'passport_series', 'patronymic', 'phone', 'policy', 'insurance_number')
