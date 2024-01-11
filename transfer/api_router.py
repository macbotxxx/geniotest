from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from transfer.api.views import UserCreationView , EmailView

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserCreationView)
router.register("test-emails", EmailView)


app_name = "api"
urlpatterns = router.urls
