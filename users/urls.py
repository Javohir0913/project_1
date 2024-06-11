from django.urls import path
from rest_framework import routers

from users.views import (
    RegisterAPIView,
    ProfileUpdateView,
    password_change_view,
    password_reset_view,
    password_reset_confirm,
    confirm_email,
    confirm_email_send_code
)

router = routers.DefaultRouter()
router.register(r'profile', ProfileUpdateView, basename='profile')
urlpatterns = [
    path('register/', RegisterAPIView.as_view(), name="register"),
    path('password-change/', password_change_view, name="password-change"),
    path('password-reset/', password_reset_view, name="password-reset"),
    path('password-reset-confirm/', password_reset_confirm, name="password-reset-confirm"),
    path('confirm-email/', confirm_email, name="confirm-email"),
    path('send-email-code/', confirm_email_send_code, name="confirm-email-send"),
] + router.urls
