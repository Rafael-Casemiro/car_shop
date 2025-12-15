from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, Group, Permission


class UserManager(BaseUserManager):
        def create_user(self, email, first_name, last_name, password=None, **extrafields):
                if not email:
                        raise ValueError("O campo Email é obrigatório")
                if not first_name:
                        raise ValueError("O campo nome é obrigatório")
                if not last_name:
                        raise ValueError("O campo sobrenome é obrigatório")
                
                email = self.normalize_email(email)

                user = self.model(
                        email=email,
                        first_name=first_name,
                        last_name=last_name,
                        password=password,
                        **extrafields
                )

                user.set_password(password)
                user.save(using=self._db)
                return user
        
        def create_superuser(self, email, first_name, last_name, password=None, **extra_fields):
                extra_fields.setdefault('is_staff', True)
                extra_fields.setdefault('is_superuser', True)
                

                if extra_fields.get('is_staff') is not True:
                        raise ValueError('Superuser deve ter is_staff=True')
                if extra_fields.get('is_superuser') is not True:
                        raise ValueError('Superuser deve ter is_superuser=True')
                
                return self.create_user(
                        email=email,
                        first_name=first_name,
                        last_name=last_name,
                        password=password,
                        **extra_fields
                )


class User(AbstractBaseUser, PermissionsMixin):
        email = models.EmailField(unique=True, verbose_name='Email')
        first_name = models.CharField(max_length=60, verbose_name='Nome')
        last_name = models.CharField(max_length=60, verbose_name='Sobrenome')
        phone = models.CharField(max_length=15, unique=True)
        date_joined = models.DateTimeField(auto_now_add=True, verbose_name='Data de Cadastro')
        is_active = models.BooleanField(default=True)
        is_staff = models.BooleanField(default=False)

        objects = UserManager()

        USERNAME_FIELD = 'email'

        REQUIRED_FIELDS = ['first_name', 'last_name', 'phone']

        class Meta:
                verbose_name = 'User'
                verbose_name_plural = 'Users'
        
        def __str__(self):
                return self.email
    
                        
