from django.contrib.auth import get_user_model
from django.db import models


# Create your models here.
class ConferenceAgenda(models.Model):
    conference_title = models.CharField(max_length=100)
    conference_description = models.TextField()
    conference_date = models.DateField()
    conference_time = models.TimeField()
    conference_place = models.CharField(max_length=100)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.conference_title}"

    class Meta:
        verbose_name = 'Conference Agenda'
        verbose_name_plural = 'Conference Agenda'
        db_table = 'conference_agenda'


class ConferenceSection(models.Model):
    conference_title = models.CharField(max_length=100)
    conference_description = models.TextField()
    conference_logo = models.ImageField(upload_to='conference_logo')
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.conference_title}"

    class Meta:
        verbose_name = 'Conference Section'
        verbose_name_plural = 'Conference Section'
        db_table = 'conference_section'
