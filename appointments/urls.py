from django.urls import path 
from . import views

urlpatterns = [
    path("appointment", views.appointment, name="appointment"),
    path("appointmentTime", views.appointmentTime, name="appointmentTime"),
    path("cancelAppointment", views.cancelAppointment, name="cancelAppointment"),
    path("completedAppointment", views.completedAppointment, name="completedAppointment"),
    path("staff", views.staff, name="staff"),
]