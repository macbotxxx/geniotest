from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import BankAccount , Balance , AccountType , BankAddress , FundingAccounts , AccountDetails

@admin.register(Balance)
class BalanceAdmin(admin.ModelAdmin):
    list_display = ('value', 'currency')
    list_display_links = ('value', 'currency')


@admin.register(AccountType)
class AccountTypeAdmin(admin.ModelAdmin):
    list_display = ('deleted', 'maintenance_fee', 'initial_deposit', 'fee_margin')
    list_display_links = ('deleted', 'maintenance_fee', 'initial_deposit', 'fee_margin')


@admin.register(BankAddress)
class BankAddressAdmin(admin.ModelAdmin):
    list_display = ('country', 'deleted', 'address_line_1')
    list_display_links = ('country', 'deleted', 'address_line_1')


@admin.register(FundingAccounts)
class FundingAccountsAdmin(admin.ModelAdmin):
    list_display = ('bank_name', 'bank_address', 'payment_type', 'identifier_type')
    list_display_links = ('bank_name', 'bank_address', 'payment_type', 'identifier_type')


@admin.register(AccountDetails)
class AccountDetailsAdmin(admin.ModelAdmin):
    list_display = ('currency', 'country', 'payment_reference',)
    list_display_links = ('currency', 'country', 'payment_reference',)



@admin.register(BankAccount)
class BankAccountAdmin(admin.ModelAdmin):
    list_display = ('account_user', 'friendly_name', 'currency', 'status','created_date')
    list_display_links = ('account_user', 'friendly_name', 'currency', 'status','created_date')
    