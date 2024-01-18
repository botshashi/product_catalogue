
from django.urls import path
from .views import register, login, users

urlpatterns = [
    path('register', register, name='register'),
    path('login', login, name='login'),
    path('users', users, name='user_list'),
]
