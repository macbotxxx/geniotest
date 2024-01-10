# Generated by Django 5.0.1 on 2024-01-04 17:01

import account.models
import django.utils.timezone
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, help_text='The unique identifier of the customer.', primary_key=True, serialize=False)),
                ('account_type', models.CharField(blank=True, choices=[('borrower', 'Borrower'), ('investor', 'Investor')], default='borrower', help_text='Account type', max_length=8, null=True, verbose_name='Account Type')),
                ('name', models.CharField(blank=True, max_length=255, verbose_name='Name of User')),
                ('email', models.EmailField(blank=True, help_text='The email address of the customer.', max_length=150, null=True, unique=True, verbose_name='Email Address')),
                ('first_name', models.CharField(blank=True, help_text='The first nammes of the customer.', max_length=50, null=True, verbose_name='First names')),
                ('last_name', models.CharField(blank=True, help_text='The last nammes of the customer.', max_length=50, null=True, verbose_name='Last names')),
                ('contact_number', models.CharField(blank=True, help_text='The contact number of the customer.', max_length=50, null=True, verbose_name='Contact number')),
                ('date_of_birth', models.DateField(blank=True, help_text='The date of birth of the customer.', null=True, verbose_name='Date of birth')),
                ('kyc_complete', models.BooleanField(default=False, help_text='Flag to determine if a cutomer have completed KYC verification', verbose_name='KYC complete')),
                ('kyc_complete_date', models.DateTimeField(blank=True, help_text='Timestamp when customer completed KYC verifiction process.', null=True, verbose_name='KYC complete date')),
                ('kyc_status', models.CharField(blank=True, choices=[('unverified', 'Unverified'), ('pending', 'Pending'), ('verified', 'Verified'), ('action_required', 'Action_required'), ('cancelled', 'Cancelled'), ('rejected', 'Rejected/Refused')], default='Unverified', help_text='The .', max_length=15, null=True, verbose_name='KYC status')),
                ('on_boarding_complete', models.BooleanField(blank=True, help_text='Flag to determine if customer has completed onboarding.', null=True, verbose_name='Completed Onboarding')),
                ('on_boarding_complete_date', models.DateField(blank=True, help_text='Timestamp when customer completed onboarding process.', null=True, verbose_name='Onboarding Complete date')),
                ('kyc_submitted', models.BooleanField(blank=True, help_text='Flag to determine if customer has submitted a KYC verification.', null=True, verbose_name='KYC submitted')),
                ('social_security_number', models.CharField(blank=True, help_text='The social security number of the customer. This helps to determine the credit score and also validates the identity of the customer. ', max_length=50, null=True, verbose_name='Social security number')),
                ('place_of_birth', models.CharField(blank=True, help_text='The place fo birth of the customer. This must match the place of birth as indicated in the cusomters photo Identification.', max_length=250, null=True, verbose_name='Place of birth')),
                ('verification_date', models.DateField(blank=True, default=django.utils.timezone.now, editable=False, help_text='Timestamp when customer is been verified.', null=True, verbose_name='Verification date')),
                ('registered_ip_address', models.GenericIPAddressField(blank=True, editable=False, help_text='The Ip address recorded at the time if registeration.', null=True, verbose_name='Registered Ip Address')),
                ('job_title', models.CharField(blank=True, help_text='The Job title of the customer. ', max_length=250, null=True, verbose_name='Job title')),
                ('default_currency_id', models.CharField(blank=True, default='EUR', help_text='The default currency of the borrower. Currency will be sent against borrowers country of residence.', max_length=3, null=True, verbose_name='Default Currency ID')),
                ('groups', models.ManyToManyField(related_name='geniotest_groups', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(related_name='geniotest_permissions', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Register User',
                'verbose_name_plural': 'Register Users',
            },
            managers=[
                ('objects', account.models.UserManager()),
            ],
        ),
    ]
