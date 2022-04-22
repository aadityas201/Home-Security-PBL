from django.urls import path
from . import views
urlpatterns = [
    path('start/' , views.home , name='home'),
    path('stream/', views.stream, name='stream')
]