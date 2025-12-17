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