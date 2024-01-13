from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from account.api.views import UserCreationView , EmailVerificationView

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("create-users", UserCreationView)
router.register("verify-email", EmailVerificationView)


app_name = "api"
urlpatterns = router.urls
