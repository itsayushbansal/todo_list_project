from django.urls import path
from rest_framework.authtoken import views as authtoken_views

from . import views


urlpatterns = [
    path('get-auth-token/', authtoken_views.obtain_auth_token, name='get-auth-token'),
    path('items/', views.toDoItemList, name="todo-items"),
    path('items/create/', views.toDoItemCreate, name="todo-item-create"),
    path('items/update/<str:pk>/', views.toDoItemUpdate, name="todo-item-update"),
    path('items/delete/<str:pk>/', views.toDoItemDelete, name="todo-item-delete"),
    path('items/<str:pk>/', views.toDoItemDetail, name="todo-item-detail"),
]
