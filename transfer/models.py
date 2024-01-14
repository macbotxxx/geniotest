import uuid
import random
import string

from django.conf import settings
from django.contrib.auth import get_user_model
from account.models import User
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db.models import CharField
from django.urls import reverse
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.db import models
from helpers.common.basemodel import BaseModel
from django.db.models.signals import post_save
from django.dispatch import receiver



NULL_AND_BLANK = {'null': True, 'blank': True}


class Balance(BaseModel):
    
    value = models.DecimalField(
        verbose_name=_("Value"),
        **NULL_AND_BLANK,
        max_digits = 300, decimal_places = 4,
        help_text=_("The unit value of the amount")
    )
    
    currency = models.CharField(
        max_length=3,
        verbose_name=_("Currency"),
        **NULL_AND_BLANK,
        default='EUR',
        help_text=_("Three digit currency code. ISO 4217 e.g. EUR for Euro")
    )

    class Meta:
        ordering = ('-created_date',)
        verbose_name = _("Balance")
        verbose_name_plural = _("Balance")


class AccountType(BaseModel):
    deleted = models.DateTimeField(
        verbose_name=_('Created'),
        **NULL_AND_BLANK,
        help_text=_(
            """Timestamp when the record was deleted. The date and time 
            are displayed in the Timezone from where request is made. 
            e.g. 2019-14-29T00:15:09Z for April 29, 2019 0:15:09 UTC"""
        )
    )

    maintenance_fee = models.DecimalField(
        verbose_name=_("Maintenance Fee"),
        **NULL_AND_BLANK,
        max_digits = 300, decimal_places = 4,
        help_text=_("The unit maintenance fee of the amount")
    )

    initial_deposit = models.DecimalField(
        verbose_name=_("Initial Deposit"),
        **NULL_AND_BLANK,
        max_digits = 300, decimal_places = 4,
        help_text=_("The initial deposit is the amount to fund you Account to activate the Account.")
    )

    fee_margin = models.DecimalField(
        verbose_name=_("Transaction Fee Margin"),
        **NULL_AND_BLANK,
        max_digits = 300, decimal_places = 4,
        help_text=_("Rate charged as transaction fee for transactions performed on Account.")
    )

    interest_rate = models.DecimalField(
        verbose_name=_("Interest Rate"),
        **NULL_AND_BLANK,
        max_digits = 300, decimal_places = 4,
        help_text=_("The interest rate of the Account type.")
    )

    auto_create = models.BooleanField(
        verbose_name = _("Auto Create"),
        default = False,
        **NULL_AND_BLANK,
        help_text=_("Toggle auto-create to allow transactions performed on Account to be completed with or without approval.")

    )

    min_balance = models.DecimalField(
        verbose_name=_("Min Balance"),
        **NULL_AND_BLANK,
        max_digits = 300, decimal_places = 4,
        help_text=_("The minimum balance a Account. Without a Account holding a minimum balance, the Account will be rendered inactive.")
    )

    max_deposit = models.DecimalField(
        verbose_name=_("Max Deposit"),
        **NULL_AND_BLANK,
        max_digits = 300, decimal_places = 4,
        help_text=_("The maximum amount to deposit on a Account")
    )

    min_deposit = models.DecimalField(
        verbose_name=_("Min Deposit"),
        **NULL_AND_BLANK,
        max_digits = 300, decimal_places = 4,
        help_text=_("The minimum amount to deposit on a Account")
    )

    max_withdrawal = models.DecimalField(
        verbose_name=_("Max Withdrawal"),
        **NULL_AND_BLANK,
        max_digits = 300, decimal_places = 4,
        help_text=_("The maximum amount to withdrawal on a Account")
    )

    min_withdrawal = models.DecimalField(
        verbose_name=_("Min Withdrawal"),
        **NULL_AND_BLANK,
        max_digits = 300, decimal_places = 4,
        help_text=_("The minimum amount to withdrawal on a Account")
    )

    allowed_currency = models.CharField(
        max_length=250,
        verbose_name=_("Allowed Currency"),
        **NULL_AND_BLANK,
        help_text=_("The currencies allowed for Account funding.")
    )

    class Meta:
        ordering = ('-created_date',)
        verbose_name = _("Bank Account Type")
        verbose_name_plural = _("Bank Account Type")



class BankAddress(BaseModel):
    
    country = models.CharField(
        max_length=3,
        verbose_name=_("Country"),
        **NULL_AND_BLANK,
        help_text=_("The two character ISO 3166-1 alpha-2 country code of the virtual account. ")
    )

    deleted = models.DateTimeField(
        verbose_name=_('Created'),
        **NULL_AND_BLANK,

        help_text=_(
            """Timestamp when the record was deleted. The date and time 
            are displayed in the Timezone from where request is made. 
            e.g. 2019-14-29T00:15:09Z for April 29, 2019 0:15:09 UTC"""
        )
    )

    address_line_1 = models.CharField(
        max_length=260,
        verbose_name=_("Address Line 1"),
        **NULL_AND_BLANK,
        help_text=_("Address line 1: street, house, apartment. ")
    )

    address_line_2 = models.CharField(
        max_length=260,
        verbose_name=_("Address Line 2"),
        **NULL_AND_BLANK,
        help_text=_("Address line 2: street, house, apartment. ")
    )

    address_line_2 = models.CharField(
        max_length=260,
        verbose_name=_("Address Line 2"),
        **NULL_AND_BLANK,
        help_text=_("Address line 2: street, house, apartment. ")
    )

    state = models.CharField(
        max_length=260,
        verbose_name=_("State"),
        **NULL_AND_BLANK,
        help_text=_("The State/Region/Province of the address.")
    )

    city = models.CharField(
        max_length=260,
        verbose_name=_("City"),
        **NULL_AND_BLANK,
        help_text=_("The city of the address.")
    )

    zip_code = models.CharField(
        max_length=260,
        verbose_name=_("Zip Code"),
        **NULL_AND_BLANK,
        help_text=_("The Zip code/Postal code of the address. Identifier consisting of a group of letters and/or numbers that is added to a postal address to assist the sorting of mail.")
    )


    class Meta:
        ordering = ('-created_date',)
        verbose_name = _("Bank Address")
        verbose_name_plural = _("Bank Address")



class FundingAccounts(BaseModel):
    
    PAYMENT_TYPE = (
        ('PRIORITY', _('PRIORITY')),
        ('REGULAR', _('REGULAR')),
    )

    ACCOUNT_NUMBER_TYPE = (
        ('IBAN', _('IBAN')),
        ('ACCOUNT_NUMBER', _('ACCOUNT_NUMBER')),
        ('INTERNATIONAL', _('INTERNATIONAL')),
    )

    IDENTIFIER_TYPE = (
        ('BIC_SWIFT', _('BIC_SWIFT')),
        ('SORT_CODE', _('SORT_CODE')),
        ('ROUTING_NUMBER', _('ROUTING_NUMBER')),
        ('ACH_ROUTING_NUMBER', _('ACH_ROUTING_NUMBER')),
        ('ROUTING_CODE', _('ROUTING_CODE')),
        ('WIRE_ROUTING_NUMBER', _('WIRE_ROUTING_NUMBER')),
    )


    bank_name = models.CharField(
        max_length=260,
        verbose_name=_("Bank Name"),
        **NULL_AND_BLANK,
        help_text=_("The name of the bank or financial institution")
    )

    bank_address = models.ForeignKey(
        'BankAddress', on_delete=models.CASCADE,
        verbose_name=_("Bank Address"),
        **NULL_AND_BLANK,
        help_text=_("The shows the bank address")
    )

    payment_type = models.CharField(
        max_length=20,
        choices=PAYMENT_TYPE,
        verbose_name=_("Payment Type"),
        **NULL_AND_BLANK,
        help_text=_("The shows the payment type when the payment will be initiated")
    )

    identifier_type = models.CharField(
        max_length=50,
        choices=IDENTIFIER_TYPE,
        verbose_name=_("Identifier Type"),
        **NULL_AND_BLANK,
        help_text=_("Depending on the payment type and country, Account code is represented by BIC/SWIFT codes, Bsb, Nsc, NSS or IFSC codes.")
    )

    identifier_value = models.CharField(
        max_length=60,
        verbose_name=_("Identifier Value"),
        **NULL_AND_BLANK,
        help_text=_("The shows the payment type when the payment will be initiated")
    )

    account_number_type = models.CharField(
        max_length=30,
        choices=ACCOUNT_NUMBER_TYPE,
        verbose_name=_("Account Number Type"),
        **NULL_AND_BLANK,
        help_text=_("The shows the account number type type when the payment will be initiated")
    )

    account_number = models.CharField(
        max_length=60,
        verbose_name=_("Account Number"),
        **NULL_AND_BLANK,
        help_text=_("The shows the payment type when the payment will be initiated")
    )

    funding_instructions = models.CharField(
        max_length=260,
        verbose_name=_("Funding Instructions"),
        **NULL_AND_BLANK,
        help_text=_("Reference ID assigned by the bank that originated the transfer to the GenioPay Account")
    )

    supported_currencies = models.TextField(
        verbose_name=_("Supported Currencies"),
        help_text = _("Array of currencies supported for the virtual account. Three-letter ISO 4217 code.")
    )

    def __str__(self):
        return str(self.bank_name)

    class Meta:
        ordering = ('-created_date',)
        verbose_name = _("Funding Accounts")
        verbose_name_plural = _("Funding Accounts")




class AccountDetails(BaseModel):
    
    currency = models.CharField(
        max_length=3,
        verbose_name=_("Currency"),
        **NULL_AND_BLANK,
        help_text=_("Three digit currency code. ISO 4217 e.g. EUR for Euro")
    )

    country = models.CharField(
        max_length=2,
        verbose_name=_("Country"),
        **NULL_AND_BLANK,
        help_text=_("The two character ISO 3166-1 alpha-2 country code of the virtual account.")
    )

    payment_reference = models.CharField(
        max_length=200,
        verbose_name=_("Payment Reference"),
        **NULL_AND_BLANK,
        help_text=_("The payment reference for the account details")
    )

    funding_accounts = models.ManyToManyField(
        'FundingAccounts',
        verbose_name=_("Funding Accounts"),
        help_text=_("The shows the funding accounts available")
    )

    class Meta:
        ordering = ('-created_date',)
        verbose_name = _("Account Details")
        verbose_name_plural = _("Account Details")




class BankAccount(BaseModel):
    id = models.UUIDField(
        verbose_name= _("ID"),
        default= uuid.uuid4,
        editable=True,
        primary_key=True,
        help_text=_("The unique identifier of an object.")
    )

    user = models.UUIDField(
        verbose_name=_("User Account"),
        **NULL_AND_BLANK,
        default= uuid.uuid4,
        help_text=_("TThe Profile ID of the User")
    )

    account_user = models.ForeignKey(
        User,on_delete=models.CASCADE,
        verbose_name=_("User Profile"),
        **NULL_AND_BLANK,
        help_text=_("The user for whom address belongs to")
    )

    friendly_name = models.CharField(
        verbose_name=_("Friendly Name"),
        **NULL_AND_BLANK,
        max_length=20,
        help_text=_("A user friendly name set to identify a Account balance")
    )

    currency = models.CharField(
        verbose_name=_("Currency"),
        **NULL_AND_BLANK,
        max_length=3,
        help_text=_("Three digit currency code. ISO 4217 e.g. EUR for Euro.")
    )

    status = models.CharField(
        verbose_name=_("Status"),
        **NULL_AND_BLANK,
        max_length=20,
        help_text=_("The status of the Account.")
    )

    requirements_type = models.CharField(
        verbose_name=_("Requirements Type"),
        **NULL_AND_BLANK,
        max_length=100,
        help_text=_("Requirements to fulfill to complete Account order.")
    )

    requirements_status = models.CharField(
        verbose_name=_("Requirements Status"),
        **NULL_AND_BLANK,
        max_length=20,
        help_text=_("Requirement type status")
    )

    available_balance = models.OneToOneField(
        Balance,
        verbose_name=_("Available Balance"),
        **NULL_AND_BLANK,
        related_name='available_balance', 
        on_delete=models.CASCADE,
        help_text=_("Funds that are at customers' disposal. Used e.g. for payment instruction acceptance. Includes bookings (positive ones scoped by valuta_date of current day or in the past, as well as negative bookings including dispositions - so independently of valuta_date), corrected on reservations (temporary funds blocks) and account limit.")
    )

    ledger_balance = models.OneToOneField(
        Balance,
        verbose_name=_("Ledger Balance"),
        **NULL_AND_BLANK,
        related_name='ledger_balance', 
        on_delete=models.CASCADE,
        help_text=_("Extended balance of the account including any pending transactions.")
    )

    pending_balance = models.OneToOneField(
        Balance,
        verbose_name=_("Pending Balance"),
        **NULL_AND_BLANK,
        related_name='pending_balance', 
        on_delete=models.CASCADE,
        help_text=_("The Pending balance of the Account")
    )

    blocked_balance = models.OneToOneField(
        Balance,
        verbose_name=_("Blocked Balance"),
        **NULL_AND_BLANK,
        related_name='blocked_balance', 
        on_delete=models.CASCADE,
        help_text=_("Blocked balance is an unsettled amount or payment. This may be an unsettled card transaction or a disputed transaction.")
    )

    total_incoming = models.OneToOneField(
        Balance,
        verbose_name=_("Total Incoming"),
        **NULL_AND_BLANK,
        related_name='total_incoming', 
        on_delete=models.CASCADE,
        help_text=_("The total amount of funds received to the Account")
    )

    default = models.BooleanField(
        verbose_name=_("Default Account"),
        **NULL_AND_BLANK,
        default = False,
        help_text=_("This defaults to False. Indicates whether Account is default account.")
    )

    account_details = models.ForeignKey(
        'AccountDetails', on_delete=models.CASCADE,
        verbose_name=_("Account Details"),
        **NULL_AND_BLANK,
        max_length=20,
        help_text=_("this store the account details for funding")
    )

    account_type = models.ForeignKey(
        'AccountType', on_delete=models.CASCADE,
        verbose_name=_("Account Type"),
        **NULL_AND_BLANK,
        max_length=20,
        help_text=_("this stores the account type")
    )

    is_linked = models.BooleanField(
        verbose_name=_("Is Linked"),
        **NULL_AND_BLANK,
        default = False,
        help_text=_("Defaults to False. If Account is imported from ASPSP connection")
    )

    has_account_details = models.BooleanField(
        verbose_name=_("Has Account Details"),
        **NULL_AND_BLANK,
        default = False,
    )

    created_date = models.DateTimeField(
        default=timezone.now,
        editable=False,
        verbose_name=_('Created'),
        help_text=_(
            """Timestamp when the record was created. The date and time 
            are displayed in the Timezone from where request is made. 
            e.g. 2019-14-29T00:15:09Z for April 29, 2019 0:15:09 UTC"""
        )
    )

    modified_date = models.DateTimeField(
        auto_now=True,
        editable=False,
        verbose_name=_('Updated'),
        **NULL_AND_BLANK,
        help_text=_(
            """Timestamp when the record was modified. The date and 
            time are displayed in the Timezone from where request 
            is made. e.g. 2019-14-29T00:15:09Z for April 29, 2019 0:15:09 UTC
            """)
    )

    
    class Meta:
        ordering = ('-created_date',)
        verbose_name = _("Bank Account")
        verbose_name_plural = _("Bank Account")










    