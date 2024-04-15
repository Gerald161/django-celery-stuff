from django.urls import path
from . import views

urlpatterns = [
    path("", views.test),
    path("schedule", views.dynamicSchedule),
    path("second-schedule", views.secondDynamicSchedule),
    path("testing", views.ProfileView.as_view()),
    path("testing2", views.ProfileView2.as_view())
]
