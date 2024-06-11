from rest_framework.permissions import IsAdminUser
from rest_framework.viewsets import ModelViewSet

from .models import SubmissionFee, About, SponsorAndPartner
from .serializers import SubmissionFeeSerializer, AboutSerializer, SponsorAndPartnerSerializer


# Create your views here.
class SubmissionFeeViewSet(ModelViewSet):
    queryset = SubmissionFee.objects.all()
    serializer_class = SubmissionFeeSerializer
    permission_classes = [IsAdminUser]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class AboutViewSet(ModelViewSet):
    queryset = About.objects.all()
    serializer_class = AboutSerializer
    permission_classes = [IsAdminUser]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class SponsorAndPartnerViewSet(ModelViewSet):
    queryset = SponsorAndPartner.objects.all()
    serializer_class = SponsorAndPartnerSerializer
    permission_classes = [IsAdminUser]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)