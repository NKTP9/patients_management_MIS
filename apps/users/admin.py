from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from apps.users.models import CustomUser
from apps.users.forms import CustomUserCreationForm, CustomUserChangeForm


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    # add_form = CustomUserCreationForm
    # form = CustomUserChangeForm

    # list_display = ['username', 'fio', 'gender', 'birth_date']

    # Add user
    add_fieldsets = (
        *UserAdmin.add_fieldsets,
        (
            'Custom fields',
            {
                'fields': (
                    'fio',
                    'gender',
                    'birth_date',
                    'groups',
                )
            }
        )
    )

    # Edit user
    fieldsets = (
        *UserAdmin.fieldsets,
        (
            'Custom fields',
            {
                'fields': (
                    'fio',
                    'gender',
                    'birth_date',
                )
            }
        )
    )

# admin.site.register(CustomUser, CustomUserAdmin)
