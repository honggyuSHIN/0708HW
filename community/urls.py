"""
URL configuration for community project.

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
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('board/',include('board.urls')),
    path('member/',include('member.urls')),

    path('dj/', include('dj_rest_auth.urls')),
    # path('dj/registration/', include('dj_rest_auth.registration.urls')),
    path('member/signup/', include('dj_rest_auth.registration.urls')),

    
    path('dj/login/', include('dj_rest_auth.urls')),
    





    # id : 7
    # honggyu04
    # asdf1234qwer
    # eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzIwMzU5NTg5LCJpYXQiOjE3MjAzNTU5ODksImp0aSI6IjczZTM4ZjFiMjBmOTQwMjZhZWE4ODFhNDIyZGRmNjMxIiwidXNlcl9pZCI6OX0.tez39dpb60w2tQZcJy2xpTmH9NLnccAwxyRB6pcKt1M
    
]
