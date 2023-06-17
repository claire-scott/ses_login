from rest_framework import viewsets 
from apps.checkin.models import Unit, UserUnit, Member, Device, EventType, Event, EventAttendance
from apps.checkin.serializers import UnitSerializer, UserUnitSerializer, MemberSerializer,EventTypeSerializer,EventSerializer,EventAttendanceSerializer

class UnitViewSet(viewsets.ModelViewSet):

    serializer_class = UnitSerializer
    queryset = Unit.objects.all()

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def get_queryset(self):
        return self.queryset()
    

class UnitViewSet(viewsets.ModelViewSet):

    serializer_class = UnitSerializer
    queryset = Unit.objects.all()

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def get_queryset(self):
        return self.queryset()
    
class EventViewSet(viewsets.ModelViewSet):
    serializer_class = EventSerializer
    queryset = Event.objects.all()

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def get_queryset(self):
        unit_list = UserUnit \
            .objects \
            .filter(user=self.request.user) \
            .values_list('unit', flat=True)
        return self.queryset().filter(unit__in=unit_list)