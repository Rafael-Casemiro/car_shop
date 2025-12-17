from django.shortcuts import render, redirect
from user.forms import RegisterForm, RegisterUpdateForm
from django.contrib import auth, messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required


def register(request):
        form = RegisterForm()

        if request.method == 'POST':
                form = RegisterForm(request.POST)

                if form.is_valid():
                        form.save()
                        messages.success(request, 'Usuário registrado')
                        return redirect('user:index')
                
        return render(
                request,
                'user/register.html',
                {
                        'form': form
                }
        )


def login_view(request):
        form = AuthenticationForm(request)
        if request.method == 'POST':
                form = AuthenticationForm(request, request.POST)

                if form.is_valid():
                        user = form.get_user()
                        auth.login(request, user)
                        messages.success(request, 'Logado com sucesso!')
                        return redirect('user:index')
                else:
                        messages.error(request, 'Login inválido')
        
        return render(
                request,
                'user/login.html',
                {
                        'form': form
                }
        )
        
