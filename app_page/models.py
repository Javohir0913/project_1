from django.contrib.auth import get_user_model
from django.db import models


# Create your models here.
class SubmissionFee(models.Model):
    submission_title = models.CharField(max_length=255)
    submission_description = models.TextField()
    submission_price = models.DecimalField(max_digits=5, decimal_places=2)
    submission_discount = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.submission_title}"

    class Meta:
        verbose_name = 'Submission Fee'
        verbose_name_plural = 'Submission Fees'
        db_table = 'submission_fee'


class About(models.Model):
    conference_coordinator = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    map_street_address = models.CharField(max_length=255)
    location_address = models.CharField(max_length=255)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.conference_coordinator}"

    class Meta:
        verbose_name = 'About'
        verbose_name_plural = 'About'
        db_table = 'about'


class SponsorAndPartner(models.Model):
    title = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='sponsor_logo')
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
