from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth import password_validation
from django.contrib.auth.forms import AuthenticationForm
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


class RegisterForm(BaseUserCreationForm):
        first_name = forms.CharField(
                required=True,
                min_length=3,
                label='Nome'
        )

        last_name = forms.CharField(
                required=True,
                min_length=3,
                label='Sobrenome'
        )

        email = forms.EmailField(
                required=True,
                widget=forms.EmailInput(attrs={
                        'placeholder': 'seu@email.com'
                })
        )

        phone = forms.CharField(
                required=True,
                min_length=11,
                label='Telefone'
        )

        class Meta:
                model = User
                fields = (
                        'first_name',
                        'last_name',
                        'email',
                        'phone'
                )
        
        def clean_email(self):
                email = self.cleaned_data.get('email', '').lower()

                if User.objects.filter(email=email).exists():
                        self.add_error(
                                'email',
                                ValidationError('Já existe esse e-mail.', code='invalid')
                        )

                return email


class RegisterUpdateForm(forms.ModelForm):
        first_name = forms.CharField(
                min_length=2,
                max_length=30,
                required=True,
                label='Nome'
        )

        last_name = forms.CharField(
                min_length=2,
                max_length=30,
                required=True,
                label='Sobrenome'
        )

        password1 = forms.CharField(
                label='Nova Senha',
                required=False,
                widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
                help_text="Deixe em branco se não quiser alterar a senha."
        )

        password2 = forms.CharField(
                label='Confirme a senha',
                required=False,
                widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        )

        class Meta:
                model = User
                fields = (
                        'first_name',
                        'last_name',
                        'email',
                        'phone',
                )
        
        def clean_email(self):
                email = self.cleaned_data.get('email', '').lower()

                if self.instance.email != email:
                        if User.objects.filter(email=email).exists():
                                raise ValidationError('Já existe este e-mail cadastrado.', code='invalid')
                
                return email


        def clean_password1(self):
                password1 = self.cleaned_data.get('password1')
                if password1:
                        try:
                                password_validation.validate_password(password1, self.instance)
                        
                        except ValidationError as error:
                                self.add_error('password1', error)
                
                return password1


        def clean(self):
                cleaned_data = super().clean()
                p1 = cleaned_data.get('password1')
                p2 = cleaned_data.get('password2')

                if p1 and p2 and p1 != p2:
                        self.add_error('password2', ValidationError('As senhas não coincidem.'))
                
                return cleaned_data
        
        def save(self, commit=True):
                user = super().save(commit=False)

                p1 = self.cleaned_data.get('password1')
                if p1:
                        user.set_password(p1)
                
                if commit:
                        user.save()
                
                return user