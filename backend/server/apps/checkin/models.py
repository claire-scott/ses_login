from django.db import models
from django.contrib.auth import get_user_model
import datetime

User = get_user_model()

class Unit(models.Model):
    name = models.TextField(blank=False)
    postcode = models.TextField(blank=True)
    linking_key = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

class Member(models.Model):
    first_name = models.TextField(blank=False)
    last_name = models.TextField(blank=False)
    member_number = models.TextField(blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User)
    deleted = models.BooleanField(default=False)

class Device(models.Model):
    name = models.TextField(blank=False)
    device_cookie = models.TextField(blank=True)
    unit = models.ForeignKey(Unit)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User)
    deleted = models.BooleanField(default=False)

class EventType(models.Model):
    event_category = models.TextField(blank=False)
    event_type = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User)
    deleted = models.BooleanField(default=False)

class Event(models.Model):
    unit = models.ForeignKey(Unit)
    event_type = models.ForeignKey(EventType)
    description = models.TextField(blank=True)
    active_from = models.DateTimeField()
    active_to = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User)
    deleted = models.BooleanField(default=False)

class EventAttendance(models.Model):
    event = models.ForeignKey(Event)
    member = models.ForeignKey(Member)
    checkin_date = models.DateTimeField(auto_now_add=True)
    checkout_date = models.DateTimeField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

"""
Non-Incident Time Capture Types
NITC tasks/events relate to any of the following items that are non-operational but inform organisation 
responsibilities of reporting:
• Training activities (including Unit training nights in order to capture skills maintenance and 
currency).
• Administration activities (required to be performed for the running of the Unit).
• Maintenance & operational audits (time spent preparing for and conducting).
• Exercises and/or skills workshops (internal and external).
• Catering/support preparations (not attached to operational events).
• Emergency Management Committee (LEMC, REMC) or Rescue Committee (LRC, RRC)
attendance.
• External and consultant forums (related to SES combat role and contribution to PPRR).
• Community Education/Public Interface events (schools, community events, promotions).
• Critical Incident Support.
"""