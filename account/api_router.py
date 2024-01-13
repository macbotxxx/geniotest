from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from account.api.views import UserCreationView , EmailVerificationView , UserInfoView

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("user-profile", UserCreationView)
router.register("user-profile/me", UserInfoView)
router.register("verify-email", EmailVerificationView)


app_name = "api"
urlpatterns = router.urls
