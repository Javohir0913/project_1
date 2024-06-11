from rest_framework import serializers

from .models import SubmissionFee, About, SponsorAndPartner


class SubmissionFeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubmissionFee
        fields = ('id', 'submission_title', 'submission_description',
                  'submission_price', 'submission_discount')


class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = ('id', 'conference_coordinator', 'phone_number', 'email', 'map_street_address', 'location_address')


class SponsorAndPartnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = SponsorAndPartner
        fields = ('id', 'title', 'logo')
