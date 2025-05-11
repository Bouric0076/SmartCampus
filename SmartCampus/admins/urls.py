# filepath: admins/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.admin_list, name='admin_list'),
    path('<int:pk>/', views.admin_detail, name='admin_detail'),
]