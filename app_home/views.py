from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.views import APIView

from app_conference.models import ConferenceAgenda, ConferenceSection
from app_conference.serializers import ConferenceAgendaSerializer, ConferenceSectionSerializer
from app_page.models import About, SponsorAndPartner, SubmissionFee
from app_page.serializers import AboutSerializer, SponsorAndPartnerSerializer, SubmissionFeeSerializer
from users.serializers import UserSerializer


# Create your views here.
class HomeView(APIView):

    def get(self, request):
        conference_agenda = ConferenceAgenda.objects.all()
        conference_section = ConferenceSection.objects.all()
        about = About.objects.all()
        sponsor_and_partner = SponsorAndPartner.objects.all()
        submission_fee = SubmissionFee.objects.all()
        users = get_user_model().objects.all()

        agenda_serializer = ConferenceAgendaSerializer(conference_agenda, many=True)
        section_serializer = ConferenceSectionSerializer(conference_section, many=True)
        about_serializer = AboutSerializer(about, many=True)
        sponsor_and_partner_serializer = SponsorAndPartnerSerializer(sponsor_and_partner, many=True)
        submission_fee_serializer = SubmissionFeeSerializer(submission_fee, many=True)
        user_serializer = UserSerializer(users, many=True)

        return Response({
            'conference_agenda': agenda_serializer.data,
            'conference_section': section_serializer.data,
            'about': about_serializer.data,
            'sponsor_and_partner': sponsor_and_partner_serializer.data,
            'submission_fee': submission_fee_serializer.data,
            'users': user_serializer.data
        })
