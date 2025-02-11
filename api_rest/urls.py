from django.urls import path

from . import views

urlpatterns = [
    path('', views.get_users, name='get_all_users'),
    path('user/<str:nick>', views.get_by_nickname),
    path('data/', views.user_manager),
]