# filepath: admins/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('list/', views.admin_list, name='admin_list'),
    path('<int:pk>/', views.admin_detail, name='admin_detail'),
    path('profile/', views.admin_profile_view, name='admin_profile'),
    path('courses/', views.course_list, name='course_list'),
    path('courses/create/', views.course_create, name='course_create'),
    path('courses/update/<int:pk>/', views.course_update, name='course_update'),
    path('courses/delete/<int:pk>/', views.course_delete, name='course_delete'),
    path('units/', views.unit_list, name='unit_list'),
    path('units/create/', views.unit_create, name='unit_create'),
    path('units/update/<int:pk>/', views.unit_update, name='unit_update'),
    path('units/delete/<int:pk>/', views.unit_delete, name='unit_delete'),
    path('timetable/', views.timetable_list, name='timetable_list'),
    path('timetable/create/', views.timetable_create, name='timetable_create'),
    path('timetable/update/<int:pk>/', views.timetable_update, name='timetable_update'),
    path('timetable/delete/<int:pk>/', views.timetable_delete, name='timetable_delete'),
    path('event/', views.event_list, name='event_list'),
    path('event/create/', views.event_create, name='event_create'),
    path('event/update/<int:pk>/', views.event_update, name='event_update'),
    path('event/delete/<int:pk>/', views.event_delete, name='event_delete'),
]