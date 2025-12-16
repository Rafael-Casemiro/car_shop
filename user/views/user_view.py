from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.db.models import Q
from user.models import User

def index(request):
        user = User.objects.all().order_by('-id')
        paginator = Paginator(user, 10)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)

        context = {
                'page_obj': page_obj,
                'site_title': 'Users - '
        }

        return render(request, 'user/index.html', context)

def user_detail(request, user_id):
        user = get_object_or_404(User, pk=user_id)

        context = {
                'user': user,
                'site_title': f'{user.first_name} - Detalhes'
        }

        return render(request, 'user/user_detail.html', context)