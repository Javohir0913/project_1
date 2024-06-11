from django.contrib import admin

from .models import SubmissionFee, About, SponsorAndPartner


# Register your models here.
admin.site.register(SubmissionFee)
admin.site.register(About)
admin.site.register(SponsorAndPartner)