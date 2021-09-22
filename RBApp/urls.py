"""RedBird URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from RBApp import views


app_name = 'RBApp'

urlpatterns = [
    path('index', views.MyIndexView.as_view(), name="my_index_view"),
    path('login', views.MyLoginView.as_view(), name="my_login_view"),
    path('signup', views.MySignUpView.as_view(), name="my_signup_view"),
    path('aboutus', views.MyAboutView.as_view(), name="my_about_view"),
    path('dashboard', views.MyDashboardView.as_view(), name="my_dashboard_view"),
    path('add-user', views.UserFormView.as_view(), name="my_userform_view"),
    path('add-dish', views.DishFormView.as_view(), name="my_dishform_view"),
    path('add-menutype', views.MenuTypeFormView.as_view(), name="my_menutypeform_view"),
]
