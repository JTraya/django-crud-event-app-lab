from django.shortcuts import render, redirect

from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView

from .models import Event, Asset
from .forms import MomentForm

class EventCreate(CreateView):
    model = Event
    fields = '__all__'

class EventUpdate(UpdateView):
    model = Event
    fields = '__all__'

class EventDelete(DeleteView):
    model = Event
    success_url = '/events/'

class AssetCreate(CreateView):
    model = Asset
    fields = '__all__'

class AssetList(ListView):
    model = Asset

class AssetDetail(DetailView):
    model = Asset

class AssetUpdate(UpdateView):
    model = Asset
    fields = '__all__'

class AssetDelete(DeleteView):
    model = Asset
    success_url = '/assets/'

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
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def event_index(request):
    events = Event.objects.all()
    return render(request, 'events/index.html', {'events': events})

def event_detail(request, event_id):
    event = Event.objects.get(id=event_id)
    moment_form = MomentForm()
    return render(request, 'events/detail.html', {'event': event, 'moment_form': moment_form})

def add_moment(request, event_id):
    form = MomentForm(request.POST)
    if form.is_valid():
        new_moment = form.save(commit=False)
        new_moment.event_id = event_id
        new_moment.save()
    return redirect('event-detail', event_id=event_id)