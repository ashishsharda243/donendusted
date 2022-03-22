from django.contrib import admin
from django.db.models.fields import DateField
from .models import DateTime, Appointment, Services
# Register your models here.
class DateTimeAdmin(admin.ModelAdmin):
    model = DateTime
    list_display = ['date', 'fromTime','fromTo']

class ServicesAdmin(admin.ModelAdmin):
    model = Services
    list_display = ['service', 'freq']

class AppointmentAdmin(admin.ModelAdmin):
    model = Appointment
    list_display = ['name', 'email','date', 'time', 'status']

admin.site.register(DateTime, DateTimeAdmin)
admin.site.register(Appointment, AppointmentAdmin)
admin.site.register(Services, ServicesAdmin)