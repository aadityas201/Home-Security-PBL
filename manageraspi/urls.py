from django.urls import path
from . import views
urlpatterns = [
    path('' , views.live_stream , name='start'),
    path('stream/', views.stream, name='stream'),
    path('stop/',views.stop,name='stop')

]