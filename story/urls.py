from django.urls import path
from .views import *

urlpatterns = [
    path('',StoryHome,name="StoryHome"),
    path('create-story/',WriteStory,name="StoyWrite"),
    path('collection/<str:cat>/', CatStoryList, name="StoyList"),
    path('read-story/<int:pk>/',ReadStory,name="ReadStory"),
]
