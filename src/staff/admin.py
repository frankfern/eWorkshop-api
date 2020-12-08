from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# from django.conf import settings
from django.utils.translation import gettext, gettext_lazy as _


from .models import Staff, Profile
from .forms import ChangeUserForm, CreateUserForm


@admin.register(Staff)
class StaffAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {
         'fields': (('first_name', 'last_name', 'email'), ('ci', 'address'), ('phone_number', 'cellphone_number'))}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {
         'fields': ('last_login', 'date_joined', 'modified')}),
    )

    form = ChangeUserForm
    add_form = CreateUserForm
    list_display = ('username', 'first_name',
                    'last_name', 'is_staff')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    search_fields = ('username', 'first_name', 'last_name', 'email')
    readonly_fields = ('modified',)


admin.site.register(Profile)
