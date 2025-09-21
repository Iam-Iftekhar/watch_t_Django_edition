from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
    
# Create your views here.
def home(request):
    return render(request, 'watch_together/home.html')

def profile(request):
    return render(request, 'watch_together/profile.html')
def watch_room(request, room_name):
    return render(request, 'watch_together/watch_room.html', {
        'room_name': room_name
    }
    )