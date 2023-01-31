from django.urls import path

from . import views


urlpatterns = [
    path('', views.all_events, name="event_list"),
]