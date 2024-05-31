from django.urls import path,include
from .views import *

urlpatterns = [
    path('',PersonHome,name="profile"),
    path('update-profile/',profile,name='updateprofile'),
    path('user-update/',userUpdate,name='userUpdate'),
    path('public/@/<int:pk>/',public_profile,name='publicprofile'),
]
