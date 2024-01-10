import uuid

from django.conf import settings

from django.contrib.auth.models import User
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db.models import CharField
from django.urls import reverse
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.db import models

# Create your models here.


class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError(_('The given email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))

        return self._create_user(email, password, **extra_fields)




class User(AbstractUser):
    """user profile for geniotest account"""


    objects = UserManager()

    # USER CHOICES

    KYC_STATUS = (
        ('unverified', _('Unverified')),
        ('pending', _('Pending')),
        ('verified', _('Verified')),
        ('action_required', _('Action_required')),
        ('cancelled', _('Cancelled')),
        ('rejected', _('Rejected/Refused'))
    )

    ACCOUNT_TYPE = (
        ('PERSONAL', _('PERSONAL')),
        ('BUSINESS', _('BUSINESS')),
    )
  
    #: First and last name do not cover name patterns around the globe
    id = models.UUIDField(
        default = uuid.uuid4,
        editable=False,
        primary_key=True,
        help_text=_("The unique identifier of the customer.")
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']
    
    account_type = CharField(
        verbose_name=_("Account Type"),
        choices=ACCOUNT_TYPE,
        default='borrower',
        blank=True,null=True,
        max_length=8,
        help_text=_("Account type"))

    name = CharField(_("Name of User"), blank=True, max_length=255)

    email = models.EmailField(
        max_length=150,
        blank=True, null=True,
        unique=True,
        verbose_name=_("Email Address"),
        help_text=_("The email address of the customer.")
    )
    
    

    username = models.CharField(
        verbose_name=_("user name"),
        max_length=50,
        blank=True,
        null=True,
        help_text=_("The user name of the customer.")
    )

    first_name = models.CharField(
        verbose_name=_("First names"),
        max_length=50,
        blank=True,
        null=True,
        help_text=_("The first names of the customer.")
    )

    last_name = models.CharField(
        max_length=50,
        verbose_name=_("Last names"),
        blank=True,
        null=True,
        help_text=_("The last names of the customer.")
    )

    
    mobile = models.CharField(
        max_length=15,
        verbose_name=_("Contact number"),
        blank=True,
        null=True,
        help_text=_("The contact number of the customer.")
    )

    date_of_birth = models.DateField(
        verbose_name=_("Date of birth"),
        blank=True,
        null=True,
        help_text=_("The date of birth of the customer.")
    )

    kyc_complete = models.BooleanField(
        verbose_name=_("KYC complete"),
        default=False,
        help_text=_("Flag to determine if a cutomer have completed KYC verification")
    )

    kyc_complete_date = models.DateTimeField(
        verbose_name=_("KYC complete date"),
        blank=True,
        null=True,
        help_text=_("Timestamp when customer completed KYC verifiction process.")
    )

    kyc_status = models.CharField(
        max_length=15,
        verbose_name=_("KYC status"),
        choices=KYC_STATUS,
        default='Unverified',
        blank=True,
        null=True,
        help_text=_("The .")
    )


    kyc_submitted = models.BooleanField(
        verbose_name=_("KYC submitted"),
        blank=True,null=True,
        help_text=_("Flag to determine if customer has submitted a KYC verification.")
    )


    place_of_birth = models.CharField(
        max_length=250,
        verbose_name=_("Place of birth"),
        blank=True, null=True,
        help_text=_("The place fo birth of the customer. This must match the place of birth as indicated in the cusomters photo Identification.")
    )

    
    country = models.CharField(
        max_length=2,
        verbose_name=_("Country of Residence"),
        blank=True, null=True,
        help_text=_("The country residence of the customer. KYC verification will be applied to this country and customer must provide proof of such residence as relevant in the country of jurisdiction.")
    )

    job_title = models.CharField(
        max_length=250,
        verbose_name=_("Job title"),
        blank=True, null=True,
        help_text=_("The Job title of the customer. ")
    )

    default_currency_id = models.CharField(
        max_length=3,
        verbose_name=_("Default Currency ID"),
        blank=True, null=True,
        default='EUR',
        help_text=_("The default currency of the borrower. Currency will be sent against borrowers country of residence.")
    )

    accept_terms = models.BooleanField(
        verbose_name=_("Default Currency ID"),
        blank=True, null=True,
        default = False,
        help_text = _("Agreements collected from the user, such as acceptance of terms and conditions, or opt in for marketing")
    )

    agreed_to_data_usage = models.BooleanField(
        verbose_name=_("Agreed to Data Usage"),
        blank=True, null=True,
        default = False,
        help_text = _("Consent to us using the provided data, including consent for us to verify the identity of relevant individuals with our service providers and database owners in accordance with the Identity Verification Terms.")
    )

    time_zone = models.CharField(
        max_length=100,
        verbose_name=_("Time Zone"),
        blank=True, null=True,
        default='Europe/London',
        help_text=_("The user Timezone is a client-specific Timezone that can be defined for the user time and user date of each individual user.")
    )

    language = models.CharField(
        max_length=3,
        verbose_name=_("Language"),
        blank=True, null=True,
        default='en',
        help_text=_("Customers language preference. All website communications will be sent out based on the users preferred language. ISO 639-1 code. Used as the language for notification emails sent by us. Defaults to the country code of the address or")
    )


    class Meta:
        verbose_name = _("Register User")
        verbose_name_plural = _("Register Users")


    def __str__(self):
        return self.email 


    def get_absolute_url(self):
        """Get url for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"username": self.pk})
