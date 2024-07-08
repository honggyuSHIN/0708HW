from django.urls import path,include

# for login
from django.urls import path
from .views import *
###

app_name='member'

urlpatterns=[
    path('login/', login_view),
    path('logout/',logout_view),
    path('info/', view=mypage),

]