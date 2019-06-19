"""run_monitor URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from . import views

urlpatterns = [
    path('runs', views.RunList.as_view(), name='run_list'),
    path('view/<int:pk>', views.RunView.as_view(), name='run_view'),
    path('edit/<int:pk>', views.RunUpdate.as_view(), name='run_edit'),
    path('delete/<int:pk>', views.RunDelete.as_view(), name='run_delete'),
    path('run_create', views.RunCreate.as_view(), name='run_form'),
    
    path('step_create/<int:pk>', views.RunStepsCreate.as_view(), name='step_form'),
    path('', views.home, name='home'),

]
