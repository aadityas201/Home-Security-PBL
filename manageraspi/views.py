from django.shortcuts import render
from django.urls import reverse

from django.http.response import StreamingHttpResponse
from .frames import VideoCamera
from django.http.response import HttpResponseRedirect
# Create your views here.

def home(request):
    return render(request, 'index.html')

def live_stream(request):
    return render(request,'stream.html')

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

def stream(request):
    return StreamingHttpResponse(gen(VideoCamera()),
                                 content_type='multipart/x-mixed-replace; boundary=frame')

def stop(request):
    return HttpResponseRedirect(reverse('home'))