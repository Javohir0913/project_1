from rest_framework.permissions import IsAdminUser
from rest_framework.viewsets import ModelViewSet

from .serializers import ConferenceAgendaSerializer, ConferenceSectionSerializer
from .models import ConferenceAgenda, ConferenceSection


# Create your views here.
class ConferenceViewSet(ModelViewSet):
    serializer_class = ConferenceAgendaSerializer
    queryset = ConferenceAgenda.objects.all()
    permission_classes = [IsAdminUser]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class ConferenceSectionViewSet(ModelViewSet):
    serializer_class = ConferenceSectionSerializer
    queryset = ConferenceSection.objects.all()
    permission_classes = [IsAdminUser]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

