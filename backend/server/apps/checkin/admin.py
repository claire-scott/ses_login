from django.contrib import admin
from .models import Unit, UserUnit, Member, Device, EventType,Event,EventAttendance

# Register your models here.
admin.site.register([Unit, 
                     UserUnit,
                     Member, 
                     Device, 
                     EventType,
                     Event,
                     EventAttendance])