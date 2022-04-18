from django.urls import include, path
from rest_framework import routers
from . import views

urlpatterns = [
    path('start/', views.Start.as_view(), name='start'),
    path('stop/', views.Stop.as_view(), name='stop'),
]
