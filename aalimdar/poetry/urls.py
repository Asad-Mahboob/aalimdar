from django.urls import path
from . import views

urlpatterns = [
    path('', views.poetry_list, name='poetry_list'),
    path('<int:pk>/', views.poetry_detail, name='poetry_detail'),
]
