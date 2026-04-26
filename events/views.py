from urllib import request

from django.contrib import messages
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.urls import reverse_lazy
from .models import Event, Category
from .forms import EventForm, CategoryForm, GroupForm
from django.db.models import Q
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.models import Group, User
from django.utils import timezone
from django.contrib.auth.decorators import login_required, user_passes_test
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView, View
from django.contrib.auth.mixins import UserPassesTestMixin
def home(request):
    return render(request, "home.html")

def is_admin(user):
    return user.is_superuser or user.groups.filter(name='Admin').exists()

def is_organizer(user):
    return user.groups.filter(name='Organizer').exists() or user.groups.filter(name='Admin').exists() or user.is_superuser

def layout(user):
    user_groups = set(user.groups.values_list("name", flat=True))

    if "Admin" in user_groups or "Organizer" in user_groups:
        return "admin/adminbase.html"
    return "base.html"

def check_role(user):
    groups = set(user.groups.values_list("name", flat=True))
    if user.is_superuser:
        return "Admin"
    elif "Admin" in groups:
        return "Admin"
    elif "Organizer" in groups:
        return "Organizer"
    else:
        return "Participant"

# Create Operations
# @user_passes_test(lambda u: is_admin(u) or is_organizer(u), login_url='home')
# def create_event(request):
#     event_form = EventForm()
    
#     if request.method == "POST":
#         event_form = EventForm(request.POST,request.FILES)
        
#         if event_form.is_valid():
#             event_form.save()
#             messages.success(request, "Event created successfully!")
#             return redirect("create_event")
#     context = {
#         "event_form": event_form,
#         "layout": layout(request.user),
#         "role": check_role(request.user),
#     }
#     return render(request, "create_event.html", context)

class CreateEvent(UserPassesTestMixin, CreateView):
    model = Event
    form_class = EventForm
    template_name = "create_event.html"
    success_url = reverse_lazy("event_list")
    
    def test_func(self):
        return is_admin(self.request.user) or is_organizer(self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["event_form"] = context.get("form")
        context["layout"] = layout(self.request.user)
        context["role"] = check_role(self.request.user)
        return context

# @user_passes_test(lambda u: is_admin(u) or is_organizer(u), login_url='home')
# def create_category(request):
#     category_form = CategoryForm()
    
#     if request.method == "POST":
#         category_form = CategoryForm(request.POST)
        
#         if category_form.is_valid():
#             category_form.save()
#             messages.success(request, "Category created successfully!")
#             return redirect("create_category")
#     context = {
#         "category_form": category_form,
#         "layout": layout(request.user),
#         "role": check_role(request.user),
#     }
#     return render(request, "create_category.html", context)

class CreateCategory(UserPassesTestMixin, CreateView):
    model = Category
    form_class = CategoryForm
    template_name = "create_category.html"
    success_url = reverse_lazy("category_list")
    
    def test_func(self):
        return is_admin(self.request.user) or is_organizer(self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["category_form"] = context.get("form")
        context["layout"] = layout(self.request.user)
        context["role"] = check_role(self.request.user)
        return context


#Update Operations
# @user_passes_test(lambda u: is_admin(u) or is_organizer(u), login_url='home')
# def update_event(request, event_id):
#     event = Event.objects.get(id=event_id)
#     event_form = EventForm(instance=event)
    
#     if request.method == "POST":
#         event_form = EventForm(request.POST, instance=event)
        
#         if event_form.is_valid():
#             event_form.save()
#             messages.success(request, "Event updated successfully!")
#             return redirect("home")
#     context = {
#         "event_form": event_form,
#         "layout": layout(request.user),
#         "role": check_role(request.user),
#     }
#     return render(request, "create_event.html", context)

class UpdateEvent(UserPassesTestMixin, UpdateView):
    model = Event
    pk_url_kwarg = "event_id"
    form_class = EventForm
    template_name = "create_event.html"
    success_url = reverse_lazy("event_list")
    
    def test_func(self):
        return is_admin(self.request.user) or is_organizer(self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["event_form"] = context.get("form")
        context["layout"] = layout(self.request.user)
        context["role"] = check_role(self.request.user)
        return context

# @user_passes_test(lambda u: is_admin(u) or is_organizer(u), login_url='home')
# def update_category(request, category_id):
#     category = Category.objects.get(id=category_id)
#     category_form = CategoryForm(instance=category)
    
#     if request.method == "POST":
#         category_form = CategoryForm(request.POST, instance=category)
        
#         if category_form.is_valid():
#             category_form.save()
#             messages.success(request, "Category updated successfully!")
#             return redirect("home")
#     context = {
#         "category_form": category_form,
#         "layout": layout(request.user),
#         "role": check_role(request.user),
#     }
#     return render(request, "create_category.html", context)

class UpdateCategory(UserPassesTestMixin, UpdateView):
    model = Category
    pk_url_kwarg = "category_id"
    form_class = CategoryForm
    template_name = "create_category.html"
    success_url = reverse_lazy("category_list")
    
    def test_func(self):
        return is_admin(self.request.user) or is_organizer(self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["category_form"] = context.get("form")
        context["layout"] = layout(self.request.user)
        context["role"] = check_role(self.request.user)
        return context


# Read Operations
# def read_events(request):
#     events = Event.objects.select_related('category').all()
#     categories = Category.objects.all()
    
#     search_query = request.GET.get('search')
#     if search_query:
#         events = events.filter(Q(name__icontains=search_query)|Q(description__icontains=search_query)|Q(location__icontains=search_query))
        

#     category_id = request.GET.get('category')
#     if category_id:
#         events = events.filter(category__id=category_id)
    
#     start_date = request.GET.get('start_date')
#     end_date = request.GET.get('end_date')
    
#     if start_date and end_date:
#         events = events.filter(date__range=[start_date, end_date])
    
#     context = {
#         "events": events,
#         "categories": categories,
#         "layout": layout(request.user),
#         "role": check_role(request.user),
#     }
#     return render(request, "read_event.html", context)

class ReadEvents(ListView):
    model = Event
    template_name = "read_event.html"
    context_object_name = "events"

    def get_queryset(self):
        events = Event.objects.select_related('category').all()
        search_query = self.request.GET.get('search')
        if search_query:
            events = events.filter(Q(name__icontains=search_query)|Q(description__icontains=search_query)|Q(location__icontains=search_query))
        
        category_id = self.request.GET.get('category')
        if category_id:
            events = events.filter(category__id=category_id)
        
        start_date = self.request.GET.get('start_date')
        end_date = self.request.GET.get('end_date')
        
        if start_date and end_date:
            events = events.filter(date__range=[start_date, end_date])
        
        return events

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        context["layout"] = layout(self.request.user)
        context["role"] = check_role(self.request.user)
        return context

# def read_categories(request):
#     categories = Category.objects.all()
#     context = {
#         "categories": categories,
#         "layout": layout(request.user),
#         "role": check_role(request.user),
#     }
#     return render(request, "read_category.html", context)

class ReadCategories(ListView):
    model = Category
    template_name = "read_category.html"
    context_object_name = "categories"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["layout"] = layout(self.request.user)
        context["role"] = check_role(self.request.user)
        return context

# def categorycal_events(request, category_id):
#     category = Category.objects.get(id=category_id)
#     events = category.events.all()
#     title = f"Events in Category: {category.name}"
    
#     context = {
#         "events": events,
#         "title": title,
#         "layout": layout(request.user),
#         "role": check_role(request.user),
#     }
#     return render(request, "read_categorycal_events.html", context)

class CategoryEvents(ListView):
    model = Event
    template_name = "read_categorycal_events.html"
    context_object_name = "events"

    def get_queryset(self):
        category_id = self.kwargs.get("category_id")
        return Event.objects.select_related('category').filter(category__id=category_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category_id = self.kwargs.get("category_id")
        category = Category.objects.get(id=category_id)
        context["title"] = f"Events in Category: {category.name}"
        context["layout"] = layout(self.request.user)
        context["role"] = check_role(self.request.user)
        return context


# def participantcal_events(request, participant_id):
    # participant = User.objects.get(id=participant_id)
    # events = participant.rsvp_events.select_related('category').all()
    # title = f"Events for Participant: {participant.username}"
    
    # context = {
    #     "events": events,
    #     "title": title,
    #     "layout": layout(request.user),
    #     "role": check_role(request.user),
    # }
    # return render(request, "read_categorycal_events.html", context)

class ParticipantEvents(ListView):
    model = Event
    template_name = "read_categorycal_events.html"
    context_object_name = "events"

    def get_queryset(self):
        self.participant = User.objects.get(id=self.kwargs.get("participant_id"))
        return self.participant.rsvp_events.select_related('category').all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = f"Events for Participant: {self.participant.username}"
        context["layout"] = layout(self.request.user)
        context["role"] = check_role(self.request.user)
        return context
    

# def event_detail(request, event_id):
#     event = Event.objects.select_related('category').get(id=event_id)
#     context = {
#         "event": event,
#         "layout": layout(request.user),
#         "role": check_role(request.user),
#     }
#     return render(request, "event_details.html", context)

class EventDetail(DetailView):
    model = Event
    template_name = "event_details.html"
    context_object_name = "event"
    pk_url_kwarg = "event_id"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["layout"] = layout(self.request.user)
        context["role"] = check_role(self.request.user)
        return context

#Delete Operations
@user_passes_test(lambda u: is_admin(u) or is_organizer(u), login_url='home')
def delete_event(request, event_id):
    event = Event.objects.get(id=event_id)
    event.delete()
    messages.success(request, "Event deleted successfully!")
    return redirect("event_list")

@user_passes_test(lambda u: is_admin(u) or is_organizer(u), login_url='home')
def delete_category(request, category_id):
    category = Category.objects.get(id=category_id)
    category.delete()
    messages.success(request, "Category deleted successfully!")
    return redirect("category_list")

@login_required
def dashboard(request):
    today = timezone.now().date()

    events = Event.objects.select_related('category')
    total_events = events.count()
    upcoming_events_count = events.filter(date__gt=today).count()
    past_events_count = events.filter(date__lt=today).count()
    rsvp_events_count = request.user.rsvp_events.select_related('category').count()

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
    elif filter_type == 'rsvp':
        filtered_events = request.user.rsvp_events.select_related('category').order_by('-date')
        table_title = "My RSVPed Events"
    else:
        filtered_events = events.order_by('-date')
        table_title = "All Events"

    context = {
        'total_events': total_events,
        'upcoming_events_count': upcoming_events_count,
        'past_events_count': past_events_count,
        'rsvp_events_count': rsvp_events_count,
        'table_title': table_title,

        'todays_events': todays_events,
        'filtered_events': filtered_events,
        "layout": layout(request.user),
        "role": check_role(request.user),
    }

    return render(request, 'dashboard.html', context)


@user_passes_test(is_admin, login_url='home')
def admin_panel(request):
    today = timezone.now().date()

    events = Event.objects.select_related('category')
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
        'total_events': total_events,
        'upcoming_events_count': upcoming_events_count,
        'past_events_count': past_events_count,
        'table_title': table_title,

        'todays_events': todays_events,
        'filtered_events': filtered_events,
        "layout": layout(request.user),
        "role": check_role(request.user),
    }
    return render(request, "admin/adminDashboard.html", context)


@user_passes_test(is_admin, login_url='home')
def all_users(request):
    users = User.objects.prefetch_related('groups').filter(groups__name='Participant').all()
    group = Group.objects.all()
    title = "Event Participants"
    context = {
        "users": users,
        "all_groups": group,
        "title": title,
        "layout": layout(request.user),
        "role": check_role(request.user),
    }
    return render(request, "admin/read_participant.html", context)

@user_passes_test(is_admin, login_url='home')
def all_organizers(request):
    users = User.objects.prefetch_related('groups').filter(groups__name='Organizer').all()
    group = Group.objects.all()
    title = "Event Organizers"
    context = {
        "users": users,
        "all_groups": group,
        "title": title,
        "role": check_role(request.user),
        "layout": layout(request.user),
    }
    return render(request, "admin/read_participant.html", context)

@user_passes_test(is_admin, login_url='home')
def create_group(request):
    form = GroupForm()
    if request.method == "POST":
        form = GroupForm(request.POST)
        if form.is_valid():
            group = form.save()
            messages.success(request, "Group created successfully!")
            return redirect("create_group")
    
    context = {
        "form": form,
        "layout": layout(request.user),
        "role": check_role(request.user),
    }
    return render(request, "admin/create_group.html", context)

@user_passes_test(is_admin, login_url='home')
def assign_user_group(request, user_id):
    if request.method == 'POST':
        user = get_object_or_404(User, id=user_id)
        group_id = request.POST.get('group_id')
        new_group = get_object_or_404(Group, id=group_id)
        
        user.groups.clear()
        user.groups.add(new_group)
        
        messages.success(request, f"{user.username} is now assigned to {new_group.name}!")
        
    return redirect('all_participants')

@user_passes_test(is_admin, login_url='home')
def all_roles_with_permissions(request):
    group = Group.objects.all()
    context = {
        "group": group,
        "layout": layout(request.user),
        "role": check_role(request.user),
    }
    return render(request, "admin/all_roles_with_permissions.html", context)


from django.core.mail import send_mail
from django.conf import settings

@login_required
def rvsp_events(request, event_id):
    event = Event.objects.get(id=event_id)

    if event.participants.filter(id=request.user.id).exists():
        subject = "Event Reminder"
        message = f"Hi {request.user.first_name},\n\nYou are already registered for {event.name} on {event.date}."
        send_mail(subject, message, settings.EMAIL_HOST_USER, [request.user.email])

        messages.warning(request, "You have already RSVPed. Reminder email sent!")

    else:
        event.participants.add(request.user)

        subject = "Event RSVP Confirmation"
        message = f"Hi {request.user.first_name},\n\nYou have successfully RSVP'd for {event.name} on {event.date}."
        send_mail(subject, message, settings.EMAIL_HOST_USER, [request.user.email])

        messages.success(request, "You have successfully RSVPed!")

    return redirect("event_detail", event_id=event.id)

def adminbase(request):
    context = {
        "role": check_role(request.user),
    }
    return render(request, "admin/adminbase.html", context)