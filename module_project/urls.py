from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('build/<int:pk>/', views.build_detail, name='build_detail'),
    path('build/create/', views.build_create, name='build_create'),
    path('build/<int:pk>/edit/', views.build_edit, name='build_edit'),
    path('build/<int:pk>/delete/', views.build_delete, name='build_delete'),
]