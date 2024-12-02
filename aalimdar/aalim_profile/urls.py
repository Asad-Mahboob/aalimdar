from django.urls import path
from . import views

urlpatterns = [
    path('', views.aalim_list, name='aalim_list'),
    path('<int:pk>/', views.aalim_detail, name='aalim_detail')
]
