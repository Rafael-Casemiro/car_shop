from django.contrib.auth.forms import UserCreationForm as BaseUserCreationForm, UserChangeForm as BaseUserChangeForm
from .models import User

# Formulário para criação de novos usuários
class CustomUserCreationForm(BaseUserCreationForm):
        class Meta:
                model = User
                fields = ('email', 'first_name', 'last_name', 'phone')

# Formulário para alteração de usuários existentes
class CustomUserChangeForm(BaseUserChangeForm):
        class Meta:
                model = User
                fields = ('email', 'first_name', 'last_name', 'phone')