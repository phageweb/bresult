"""bridge URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from bresult import views
from bresult.views import PersonList, AboutView
from django.contrib import admin
from django.conf.urls import include



urlpatterns = [
    url(r'^about/$',    AboutView.as_view()),
    url(r'persons/$',   PersonList.as_view()),
    url(r'^admin/',     include(admin.site.urls)),
    url(r'^accounts/', include('registration.urls')),
    #    url(r'^login/$', AboutView.as_view()),
]
