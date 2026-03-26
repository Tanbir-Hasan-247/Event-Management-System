from django.urls import path
from . import views

urlpatterns = [
    path("create_event/", views.create_event, name="create_event"),
    path("create_category/", views.create_category, name="create_category"),
    path("create_participant/", views.create_participant, name="create_participant"),
]