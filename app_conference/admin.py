from django.contrib import admin

from .models import ConferenceAgenda, ConferenceSection


# Register your models here.
admin.site.register(ConferenceAgenda)
admin.site.register(ConferenceSection)