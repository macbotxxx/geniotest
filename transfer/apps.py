from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class TransferConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'transfer'
    verbose_name = _('Bank Account Info')
