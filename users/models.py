from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class CustomUser(AbstractUser):
    username = models.EmailField(unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_day = models.DateField(blank=True, null=True)
    phone_number = models.CharField(max_length=20, unique=True)
    gender = models.CharField(max_length=15)
    affiliation = models.TextField()
    photo = models.ImageField(upload_to='users_photo/', blank=True, null=True)
    confirmed_email = models.BooleanField(default=False)

    def __str__(self):
        return str(self.username)

    class Meta:
        db_table = 'users'
        verbose_name = 'User'
        verbose_name_plural = 'Users'


class PasswordResets(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    reset_code = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)

    class Meta:
        db_table = 'password_resets'
        unique_together = (('user', 'created_at'),)
        index_together = (('user', 'created_at'),)
        verbose_name = 'Password Reset'
        verbose_name_plural = 'Password Resets'


class ConfirmEmailModel(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    confirm_code = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)

    class Meta:
        db_table = 'confirmation_email'
        unique_together = (('user', 'created_at'),)
        index_together = (('user', 'created_at'),)
        verbose_name = 'Confirm Email'
        verbose_name_plural = 'Confirm Emails'
