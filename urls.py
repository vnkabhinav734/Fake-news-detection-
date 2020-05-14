"""appointment URL Configuration

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
    path('', views.home, name="Welcome"),
    path('user', views.userlogin, name="userlogin"),
    path('ureg', views.uregistraction, name="UserReg"),
    path('uregaction', views.uregaction, name="uregaction"),
    path('ulogin', views.ulogin, name="ulogin"),
    path('uhome', views.uhome, name="uhome"),
    path('ulogout', views.ulogout, name="ulogout"),
    path('newssearch', views.newssearch, name="newssearch"),
    path('viewpprofile', views.viewpprofile, name="viewpprofile"),
    path('searchnews', views.searchnews, name="searchnews"),
    path('tfidfcalc', views.tfidfcalc, name="tfidfcalc"),
    path('ldaaction', views.ldaaction, name="ldaaction"),
    path('test', views.test, name="test"),
    

    
]
