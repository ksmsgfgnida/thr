"""
URL configuration for djangoProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views
from .views import category_performance_list
from .views import register_view, login_view
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('', views.index, name='index'),
    path('category/<str:category_id>/', category_performance_list, name='category_performance_list'),
    path('performances/', views.performance_list, name='performance_list'),
    path('performances/create/', views.performance_create, name='performance_create'),
    path('performances/<int:pk>/', views.performance_detail, name='performance_detail'),
    path('performances/<int:pk>/update/', views.performance_update, name='performance_update'),
    path('performances/<int:pk>/delete/', views.performance_delete, name='performance_delete'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
]
