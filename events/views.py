from pyexpat.errors import messages

from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Event, Participant, Category
from .forms import EventForm, ParticipantForm, CategoryForm

# Create your views here.

def create_event(request):
    event_form = EventForm()
    category_form = CategoryForm()
    
    if request.method == "POST":
        event_form = EventForm(request.POST)
        category_form = CategoryForm(request.POST)
        
        if event_form.is_valid() and category_form.is_valid():
            event = event_form.save()
            category = category_form.save(commit=False)
            category.events=event
            category.save()
            messages.success(request, "Event created successfully!")
            return redirect("create_event")
    context = {
        "event_form": event_form,
        "category_form": category_form
    }
    return render(request, "create_event.html", context)

def create_category(request):
    category_form = CategoryForm()
    
    if request.method == "POST":
        category_form = CategoryForm(request.POST)
        
        if category_form.is_valid():
            category_form.save()
            messages.success(request, "Category created successfully!")
            return redirect("create_category")
    context = {
        "category_form": category_form
    }
    return render(request, "create_category.html", context)


def create_participant(request):
    participant_form = ParticipantForm()
    event_form = EventForm()
    
    if request.method == "POST":
        participant_form = ParticipantForm(request.POST)
        event_form = EventForm(request.POST)
        
        if participant_form.is_valid() and event_form.is_valid():
            participant = participant_form.save()
            event = event_form.save(commit=False)
            event.participants=participant
            event.save()
            messages.success(request, "Participant created successfully!")
            return redirect("create_participant")
    context = {
        "participant_form": participant_form,
        "event_form": event_form
    }
    return render(request, "create_participant.html", context)