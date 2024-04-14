from django.urls import path
from . import views

urlpatterns = [
    path("", views.test),
    path("schedule", views.dynamicSchedule),
    path("second-schedule", views.secondDynamicSchedule)
]
