from rest_framework import serializers

from .models import ConferenceAgenda, ConferenceSection


class ConferenceAgendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConferenceAgenda
        fields = ('id', 'conference_title', 'conference_description',
                  'conference_date', 'conference_time', 'conference_place')


class ConferenceSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConferenceSection
        fields = ('id', 'conference_title', 'conference_description', 'conference_logo')
