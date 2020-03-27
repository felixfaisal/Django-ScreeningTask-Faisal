from django.urls import path 
from .views import *

urlpatterns=[
    path('',home,name='home'),
    path('list/',list,name='list'),
    path('api/video',VideoAPI.as_view()),
    path('api/chunk',ChunkAPI.as_view())
]