"""core URL Configuration

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
from django.urls import path, include
from webapi import views
from django.shortcuts import redirect
from rest_framework_swagger.views import get_swagger_view

def redirect_index(request):
    return redirect('index')



schema_view = get_swagger_view(title='DOC API')


urlpatterns = [
    path('', views.index, name="index"),
    path('report', views.report, name="report"),
    path('api/', include('webapi.urls')),
    path('docs/', schema_view),
    path('api-auth/', include('rest_framework.urls')),
    path('accounts/profile/', redirect_index)
]
