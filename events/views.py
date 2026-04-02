from django.contrib import messages
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Event, Participant, Category
from .forms import EventForm, ParticipantForm, CategoryForm
from django.db.models import Q
# Create your views here.

from django.shortcuts import render
from django.utils import timezone
from .models import Event, Participant

def home(request):
    return render(request, "home.html")

# Create Operations
def create_event(request):
    event_form = EventForm()
    
    if request.method == "POST":
        event_form = EventForm(request.POST)
        
        if event_form.is_valid():
            event_form.save()
            messages.success(request, "Event created successfully!")
            return redirect("create_event")
    context = {
        "event_form": event_form,
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
    
    if request.method == "POST":
        participant_form = ParticipantForm(request.POST)
        
        if participant_form.is_valid() and participant_form.cleaned_data['event']:
            participant = participant_form.save()
            
            events = participant_form.cleaned_data['event']
            for event in events:
                event.participants.add(participant)
            messages.success(request, "Participant created successfully!")
            return redirect("create_participant")
            
    context = {
        "participant_form": participant_form,
    }
    return render(request, "create_participant.html", context)


#Update Operations
def update_event(request, event_id):
    event = Event.objects.get(id=event_id)
    event_form = EventForm(instance=event)
    
    if request.method == "POST":
        event_form = EventForm(request.POST, instance=event)
        
        if event_form.is_valid():
            event_form.save()
            messages.success(request, "Event updated successfully!")
            return redirect("home")
    context = {
        "event_form": event_form,
    }
    return render(request, "create_event.html", context)

def update_category(request, category_id):
    category = Category.objects.get(id=category_id)
    category_form = CategoryForm(instance=category)
    
    if request.method == "POST":
        category_form = CategoryForm(request.POST, instance=category)
        
        if category_form.is_valid():
            category_form.save()
            messages.success(request, "Category updated successfully!")
            return redirect("home")
    context = {
        "category_form": category_form,
    }
    return render(request, "create_category.html", context)

def update_participant(request, participant_id):
    participant = Participant.objects.get(id=participant_id)
    participant_form = ParticipantForm(instance=participant)
    
    if request.method == "POST":
        participant_form = ParticipantForm(request.POST, instance=participant)
        
        if participant_form.is_valid() and participant_form.cleaned_data['event']:
            participant_form.save()
            events = participant_form.cleaned_data['event']
            for event in events:
                event.participants.add(participant)
            messages.success(request, "Participant updated successfully!")
            return redirect("home")
    context = {
        "participant_form": participant_form,
    }
    return render(request, "create_participant.html", context)

# Read Operations
def read_events(request):
    events = Event.objects.select_related('category').prefetch_related('participants').all()
    categories = Category.objects.all()
    
    search_query = request.GET.get('search')
    if search_query:
        events = events.filter(Q(name__icontains=search_query)|Q(description__icontains=search_query)|Q(location__icontains=search_query))
        

    category_id = request.GET.get('category')
    if category_id:
        events = events.filter(category__id=category_id)
    
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')
    
    if start_date and end_date:
        events = events.filter(date__range=[start_date, end_date])
    
    context = {
        "events": events,
        "categories": categories,
    }
    return render(request, "read_event.html", context)

def read_categories(request):
    categories = Category.objects.all()
    context = {
        "categories": categories,
    }
    return render(request, "read_category.html", context)

def read_participants(request):
    participants = Participant.objects.prefetch_related('event').all()
    context = {
        "participants": participants,
    }
    return render(request, "read_participant.html", context)

def categorycal_events(request, category_id):
    category = Category.objects.get(id=category_id)
    events = category.events.prefetch_related('participants').all()
    title = f"Events in Category: {category.name}"
    
    context = {
        "events": events,
        "title": title,
    }
    return render(request, "read_categorycal_events.html", context)

def participantcal_events(request, participant_id):
    participant = Participant.objects.get(id=participant_id)
    events = participant.event.select_related('category').all()
    title = f"Events for Participant: {participant.name}"
    
    context = {
        "events": events,
        "title": title,
    }
    return render(request, "read_categorycal_events.html", context)

def event_detail(request, event_id):
    event = Event.objects.select_related('category').prefetch_related('participants').get(id=event_id)
    context = {
        "event": event,
    }
    return render(request, "event_details.html", context)

#Delete Operations
def delete_event(request, event_id):
    event = Event.objects.get(id=event_id)
    event.delete()
    messages.success(request, "Event deleted successfully!")
    return redirect("event_list")

def delete_category(request, category_id):
    category = Category.objects.get(id=category_id)
    category.delete()
    messages.success(request, "Category deleted successfully!")
    return redirect("category_list")

def delete_participant(request, participant_id):
    participant = Participant.objects.get(id=participant_id)
    participant.delete()
    messages.success(request, "Participant deleted successfully!")
    return redirect("participant_list")

def dashboard(request):
    today = timezone.now().date()

    events = Event.objects.select_related('category')
    total_participants = Participant.objects.count()
    total_events = events.count()
    upcoming_events_count = events.filter(date__gt=today).count()
    past_events_count = events.filter(date__lt=today).count()

    todays_events = events.filter(date=today)
   
    filter_type = request.GET.get('filter')
    filtered_events = events.order_by('-date')
    table_title = "All Events"
    if filter_type == 'upcoming':
        filtered_events = events.filter(date__gt=today).order_by('date')
        table_title = "Upcoming Events"
    elif filter_type == 'past':
        filtered_events = events.filter(date__lt=today).order_by('-date')
        table_title = "Past Events"
    else:
        filtered_events = events.order_by('-date')
        table_title = "All Events"

    context = {
        'total_participants': total_participants,
        'total_events': total_events,
        'upcoming_events_count': upcoming_events_count,
        'past_events_count': past_events_count,
        'table_title': table_title,

        'todays_events': todays_events,
        'filtered_events': filtered_events,
    }

    return render(request, 'dashboard.html', context)
