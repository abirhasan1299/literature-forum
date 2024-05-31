from django.urls import path
from .views import home,fetchData

urlpatterns = [
    path('',home,name="demo"),
    path('fetch/',fetchData,name="fetch")
]
