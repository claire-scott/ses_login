from rest_framework import serializers
from apps.checkin.models import Unit, UserUnit, Member, Device, EventType, Event, EventAttendance

class UnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unit
        read_only_fields = (
            "id",
            "created_at",
            "created_by",
        )
        fields = (
            "id",
            "name",
            "postcode",
            "linking_key",
            "created_at",
            "created_by",
        )

class UserUnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserUnit
        read_only_fields = (
            "id",
            "created_at",
            "created_by",
        )
        fields = (
            "id",
            "unit",
            "user",
            "created_at",
            "deleted",
        )

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        read_only_fields = (
            "id",
            "created_at",
            "created_by",
        )
        fields = (
            "id",
            "first_name",
            "last_name",
            "member_number",
            "created_at",
            "created_by",
            "deleted",
        )

class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        read_only_fields = (
            "id",
            "created_at",
            "created_by",
        )
        fields = (
            "id",
            "name",
            "device_cookie",
            "unit",
            "postcode",
            "linking_key",
            "created_at",
            "created_by",
            "deleted",
        )

class EventTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventType
        read_only_fields = (
            "id",
            "created_at",
            "created_by",
        )
        fields = (
            "id",
            "event_category",
            "event_type",
            "created_at",
            "created_by",
            "deleted",
        )

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        read_only_fields = (
            "id",
            "created_at",
            "created_by",
        )
        fields = (
            "id",
            "unit",
            "event_type",
            "description",
            "active_from",
            "active_to",
            "created_at",
            "created_by",
            "deleted",
        )

class EventAttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventAttendance
        read_only_fields = (
            "id",
            "created_at"
        )
        fields = (
            "id",
            "event",
            "member",
            "checkin_date",
            "checkout_date",
            "created_at",
        )