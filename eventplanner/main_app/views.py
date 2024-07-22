from django.shortcuts import render

from django.http import HttpResponse

from .models import Event

# class Event:
#     def __init__(self, name, type, description, people):
#         self.name = name
#         self.type = type
#         self.description = description
#         self.people = people

# events = [
#     Event('Company Meeting', 'Business', 'Discussing business analytics', 25),
#     Event('Basketball Tournament', 'Competition', 'Bracket style basketball tournament', 56),
#     Event('Jones Wedding Reception', 'Ceremony', 'Wedding reception', 200)

# ]

# Create your views here.
def home(request):
    return HttpResponse('<h1>Hello!</h1>')

def about(request):
    return render(request, 'about.html')

def event_index(request):
    events = Event.objects.all()
    return render(request, 'events/index.html', {'events': events})

def event_detail(request, event_id):
    event = Event.objects.get(id=event_id)
    return render(request, 'events/detail.html', {'event': event})