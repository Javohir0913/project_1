from rest_framework import routers

from .views import ConferenceViewSet, ConferenceSectionViewSet

router = routers.DefaultRouter()

router.register(r'agenda', ConferenceViewSet)
router.register(r'section', ConferenceSectionViewSet)

urlpatterns = router.urls
