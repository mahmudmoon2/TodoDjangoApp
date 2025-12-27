from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('register/' , views.register, name='register'),
    path('login/' , views.login_view, name='login'),
    path('logout/' , views.logout_view, name='logout'),
    path('create/' , views.task_create, name='create'), 
    path('tasks/<int:task_id>/', views.task_detail, name='task_detail'),
    path('delete/<int:task_id>/', views.task_delete, name='delete'),
    path('toggle-status/<int:task_id>/', views.toggle_task_status, name='toggle_status'),
    
]
