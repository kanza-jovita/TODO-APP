from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('todo/<int:todo_id>/', views.detail, name='detail'),
    path('add/', views.add, name='add'),
    path('edit/<int:todo_id>/', views.edit, name='edit'),
    path('delete/<int:todo_id>/', views.delete, name='delete'),
]
