from django.contrib import admin
from .models import Unit, Member, Device, EventType,Event,EventAttendance

# Register your models here.
admin.site.register([Unit, 
                     Member, 
                     Device, 
                     EventType,
                     Event,
                     EventAttendance])