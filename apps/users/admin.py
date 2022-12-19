from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from apps.users.models import CustomUser
from apps.users.forms import CustomUserCreationForm, CustomUserChangeForm


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    inlines = []

    model = CustomUser
    # add_form = CustomUserCreationForm
    # form = CustomUserChangeForm

    list_display = ['username', 'email', 'first_name', 'last_name', 'passport_number',
                    'passport_series', 'patronymic', 'phone', 'policy', 'insurance_number']

    # Add user
    add_fieldsets = (
        *UserAdmin.add_fieldsets,
        (
            'Custom fields',
            {
                'fields': (
                    'passport_number',
                    'passport_series',
                    'patronymic',
                    'phone',
                    'policy',
                    'insurance_number',
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
                    'passport_number',
                    'passport_series',
                    'patronymic',
                    'phone',
                    'policy',
                    'insurance_number',
                )
            }
        )
    )

    def user_groups_display(self, user):
        try:
            groups = []
            for group in user.groups.all():
                groups.append(group.name)
            return ', '.join(groups)
        except:
            return '-'

    def get_inlines(self, request, obj):
        if obj is not None:
            print(obj)
            # if user in Врач group, display inline form
            # if obj.groups.filter(name='Врач').exists():
            #     return [DoctorWorkScheduleInline]
        return []

    # def get_form(self, request, obj=None, **kwargs):
    #     form = super().get_form(request, obj, **kwargs)
    #     # if user in Врач group, display inline form
    #     # if obj.groups.filter(name='Врач').exists():
    #     #     pass
    #     return form


# admin.site.register(CustomUser, CustomUserAdmin)
