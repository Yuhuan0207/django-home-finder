"""homefinder URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, re_path
from . import views

app_name = 'homesapp'

urlpatterns = [    
    #/homesapp/
    re_path(r'^$', views.IndexView.as_view(), name='index'),
    #/homesapp/1
    re_path(r'^(?P<pk>[0-9]+)/$', views.LocationView.as_view(), name = 'property'),
    #/homesapp/1/2
    re_path(r'^[0-9]+/(?P<pk>[0-9]+)/$', views.PropertyView.as_view(), name = 'propertyview')
]
