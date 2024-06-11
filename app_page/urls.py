from rest_framework import routers

from .views import SubmissionFeeViewSet, AboutViewSet, SponsorAndPartnerViewSet


router = routers.DefaultRouter()

router.register(r'submissions', SubmissionFeeViewSet)
router.register(r'about', AboutViewSet)
router.register(r'sponsor', SponsorAndPartnerViewSet)


urlpatterns = router.urls
