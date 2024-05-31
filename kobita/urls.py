from django.urls import path
from .views import *

urlpatterns = [
    path('',KobitaHome,name="HomeKobita"),
    path('create-poem/',WritePoem,name="CreatePoem"),
    path('read-poem/<int:pk>/<str:name>/',readpoem,name="readpoem"),
]
