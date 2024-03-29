from django.conf import settings
from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.auth import get_user_model, decorators
from django.utils.translation import gettext_lazy as _
from .models import Wallet


User = get_user_model()



@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):
    # form = UserAdminChangeForm
    # add_form = UserAdminCreationForm
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (_("Personal info"), {
            "fields": ('account_type','first_name', 'last_name', 'mobile', 'date_of_birth', 'kyc_complete', 'kyc_complete_date', 'kyc_status', 'kyc_submitted', 'place_of_birth', 'country', 'job_title', 'default_currency_id','accept_terms', 'agreed_to_data_usage', 'time_zone', 'language',)}),

        (_("GenioPay Account Details"), {
            "fields": (
                'geniopay_user_id', 
                'geniopay_key',
                'email_verification',
                )}),

        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    list_display = ["email", "name", "is_superuser"]
    search_fields = ["name"]
    ordering = ["id"]
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2"),
            },
        ),
    )


@admin.register(Wallet)
class WalletAdmin(admin.ModelAdmin):
    list_display = ('user', 'balance', 'wallet_id')
    list_display_links = ('user', 'balance', 'wallet_id')