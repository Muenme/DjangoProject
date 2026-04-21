from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('build/<int:pk>/', views.build_detail, name='build_detail'),
]