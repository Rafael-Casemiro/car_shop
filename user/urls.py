from django.urls import path, include
from user.views import user_view, user_form

app_name = 'user'

urlpatterns = [
    path('', user_view.index , name='index'),
    path('user/<int:user_id>/', user_view.user_detail, name='user'),
    path('user/cadastro/', user_form.register, name='cadastro')
]
