from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User
from .forms import CustomUserCreationForm, CustomUserChangeForm

class UserAdmin(BaseUserAdmin):
        form = CustomUserChangeForm
        add_form = CustomUserCreationForm

        list_display = ('email', 'first_name', 'last_name', 'phone', 'is_staff')
        list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')

        search_fields = ('email', 'first_name', 'phone')
        ordering = ('email',)

        fieldsets = (
                (None, {'fields': ('email', 'password')}),
                ('Informações Pessoais', {'fields': ('first_name', 'last_name', 'phone')}),
                ('Permissões', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
                ('Datas', {'fields': ('last_login', 'date_joined')})
        )

        add_fieldsets = (
                (None, {
                        'classes': ('wide',),
                        'fields': ('email', 'first_name', 'last_name', 'phone', 'password', 'confirm_password'),
                })
        )

admin.site.register(User, UserAdmin)