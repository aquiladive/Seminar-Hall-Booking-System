"""
URL configuration for sbhs project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from sbhs.views import *

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('home/', home),
    path('hall/', hall),
    path('about/', about),
    path('login/', deptlogin),
    path('dept/', dept),
    path('adminlogin/', adminlogin),
    path('admin/', admin),
    path('event_database/', adminApprove),
    path('book_event/', bookEvent),
    path('book_event/success/', bookSuccess),
    re_path(r'^event_cal1/$', CalendarViewR.as_view()),
    re_path(r'^event_cal2/$', CalendarViewT.as_view()),
]
