from django.shortcuts import render
from .models import Events

def all_events(request):
    events = Events.get_all()
    context = {'events': events}
    return render(request, 'events/event_list.html', context)