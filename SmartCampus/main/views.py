from django.shortcuts import render
from admins.models import Notice, Event

# Create your views here.

def home(request):
    notices = Notice.objects.order_by('-date_posted')[:3]
    events = Event.objects.order_by('-date_posted')[:3]
    return render(request, 'main/home.html', {
        'notices': notices,
        'events': events,
    })
