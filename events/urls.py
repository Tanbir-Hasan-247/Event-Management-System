from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("create_event/", views.create_event, name="create_event"),
    path("create_category/", views.create_category, name="create_category"),
    path("create_participant/", views.create_participant, name="create_participant"),
    path("update_event/<int:event_id>/", views.update_event, name="update_event"),
    path("update_category/<int:category_id>/", views.update_category, name="update_category"),
    path("update_participant/<int:participant_id>/", views.update_participant, name="update_participant"),
    path("event_list/", views.read_events, name="event_list"),
    path("category_list/", views.read_categories, name="category_list"),
    path("participant_list/", views.read_participants, name="participant_list"),
    path("event/<int:event_id>/", views.event_detail, name="event_detail"),
    path("category/<int:category_id>/events/", views.categorycal_events, name="categorycal_events"),
    path("participant/<int:participant_id>/events/", views.participantcal_events, name="participantcal_events"),
    path("delete_event/<int:event_id>/", views.delete_event, name="delete_event"),
    path("delete_category/<int:category_id>/", views.delete_category, name="delete_category"),
    path("delete_participant/<int:participant_id>/", views.delete_participant, name="delete_participant"),
]