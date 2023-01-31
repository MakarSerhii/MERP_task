from django.urls import path

from . import views


urlpatterns = [
    path('', views.profile, name="profile"),
] + [
    path('user_list/', views.event_list),
    path('<int:id>', views.event_api),
]
