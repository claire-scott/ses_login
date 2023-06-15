from rest_framework import viewsets 
from apps.checkin.models import Unit, Member, Device, EventType, Event, EventAttendance
from apps.checkin.serializers import UnitSerializer, MemberSerializer,EventTypeSerializer,EventSerializer,EventAttendanceSerializer

class UnitViewSet(viewsets.ModelViewSet):

    serializer_class = UnitSerializer
    queryset = Unit.objects.all()

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def get_queryset(self):
        return self.queryset()