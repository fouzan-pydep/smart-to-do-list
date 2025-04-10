# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('home/',views.home,name='home'),
    path('add/',views.task_create,name='task_create'),
    path('com/',views.task_list,name='task_list'),
    path('complete/<int:pk>/', views.task_complete, name='task_complete'),
    path('delete/<int:pk>/', views.task_delete, name='task_delete'),
    path('high/', views.task_high, name='high'),
    path('highss/', views.task_high_list, name='task_high_list'),
    path('high/update/<int:pk>/', views.task_high_update, name='task_high_update'),
    path('high/delete/<int:pk>/', views.task_high_delete, name='task_high_delete'),
    path('medium/', views.task_medium, name='medium'),
    path('mediumss/', views.task_medium_list, name='task_medium_list'),
    path('medium/update/<int:pk>/', views.task_medium_update, name='task_medium_update'),
    path('medium/delete/<int:pk>/', views.task_medium_delete, name='task_medium_delete'),
    path('low/', views.task_delow, name='low'),
        path('tasks/low/edit/<int:pk>/', views.edit_low_task, name='edit_low_task'),
    path('tasks/low/delete/<int:pk>/', views.delete_low_task, name='delete_low_task'),
]
 