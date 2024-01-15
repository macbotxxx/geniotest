from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from transfer.api.views import BankAccountView , SendFundsView

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("virtual-account", BankAccountView)
router.register("transfer-funds", SendFundsView)



app_name = "virtual_account"
urlpatterns = router.urls
