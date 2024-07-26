from django.shortcuts import render, redirect

from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Event, Asset
from .forms import MomentForm

class Home(LoginView):
    template_name = 'home.html'

class EventCreate(LoginRequiredMixin, CreateView):
    model = Event
    fields = ['name', 'type', 'description', 'people']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class EventUpdate(LoginRequiredMixin, UpdateView):
    model = Event
    fields = ['name', 'type', 'description', 'people']

class EventDelete(LoginRequiredMixin, DeleteView):
    model = Event
    success_url = '/events/'

class AssetCreate(LoginRequiredMixin, CreateView):
    model = Asset
    fields = '__all__'

class AssetList(LoginRequiredMixin, ListView):
    model = Asset

class AssetDetail(LoginRequiredMixin, DetailView):
    model = Asset

class AssetUpdate(LoginRequiredMixin, UpdateView):
    model = Asset
    fields = '__all__'

class AssetDelete(LoginRequiredMixin, DeleteView):
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
# def home(request):
#     return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

@login_required
def event_index(request):
    events = Event.objects.filter(user=request.user)
    return render(request, 'events/index.html', {'events': events})

@login_required
def event_detail(request, event_id):
    event = Event.objects.get(id=event_id)
    assets_event_doesnt_have = Asset.objects.exclude(id__in = event.assets.all().values_list('id'))
    moment_form = MomentForm()
    return render(request, 'events/detail.html', {
        'event': event, 
        'moment_form': moment_form,
        'assets': assets_event_doesnt_have
        })

@login_required
def add_moment(request, event_id):
    form = MomentForm(request.POST)
    if form.is_valid():
        new_moment = form.save(commit=False)
        new_moment.event_id = event_id
        new_moment.save()
    return redirect('event-detail', event_id=event_id)

@login_required
def associate_asset(request, event_id, asset_id):
    Event.objects.get(id=event_id).assets.add(asset_id)
    return redirect('event-detail', event_id=event_id)

@login_required
def remove_asset(request, event_id, asset_id):
    Event.objects.get(id=event_id).assets.remove(asset_id)
    return redirect('event-detail', event_id=event_id)

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('event-index')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error-message': error_message}
    return render(request, 'signup.html', context)