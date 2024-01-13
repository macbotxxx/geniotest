# Generated by Django 4.2.9 on 2024-01-13 13:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AccountDetails',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, help_text='The unique identifier of an object.', primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, editable=False, help_text='Timestamp when the record was created. The date and time \n            are displayed in the Timezone from where request is made. \n            e.g. 2019-14-29T00:15:09Z for April 29, 2019 0:15:09 UTC', verbose_name='Created')),
                ('modified_date', models.DateTimeField(auto_now=True, help_text='Timestamp when the record was modified. The date and \n            time are displayed in the Timezone from where request \n            is made. e.g. 2019-14-29T00:15:09Z for April 29, 2019 0:15:09 UTC\n            ', null=True, verbose_name='Updated')),
                ('currency', models.CharField(blank=True, help_text='Three digit currency code. ISO 4217 e.g. EUR for Euro', max_length=3, null=True, verbose_name='Currency')),
                ('country', models.CharField(blank=True, help_text='The two character ISO 3166-1 alpha-2 country code of the virtual account.', max_length=2, null=True, verbose_name='Country')),
                ('payment_reference', models.CharField(blank=True, help_text='The payment reference for the account details', max_length=200, null=True, verbose_name='Payment Reference')),
            ],
            options={
                'verbose_name': 'Account Details',
                'verbose_name_plural': 'Account Details',
                'ordering': ('-created_date',),
            },
        ),
        migrations.CreateModel(
            name='AccountType',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, help_text='The unique identifier of an object.', primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, editable=False, help_text='Timestamp when the record was created. The date and time \n            are displayed in the Timezone from where request is made. \n            e.g. 2019-14-29T00:15:09Z for April 29, 2019 0:15:09 UTC', verbose_name='Created')),
                ('modified_date', models.DateTimeField(auto_now=True, help_text='Timestamp when the record was modified. The date and \n            time are displayed in the Timezone from where request \n            is made. e.g. 2019-14-29T00:15:09Z for April 29, 2019 0:15:09 UTC\n            ', null=True, verbose_name='Updated')),
                ('deleted', models.DateTimeField(help_text='Timestamp when the record was deleted. The date and time \n            are displayed in the Timezone from where request is made. \n            e.g. 2019-14-29T00:15:09Z for April 29, 2019 0:15:09 UTC', verbose_name='Created')),
                ('maintenance_fee', models.DecimalField(blank=True, decimal_places=2, help_text='The unit maintenance fee of the amount', max_digits=300, null=True, verbose_name='Maintenance Fee')),
                ('initial_deposit', models.DecimalField(blank=True, decimal_places=2, help_text='The initial deposit is the amount to fund you Account to activate the Account.', max_digits=300, null=True, verbose_name='Initial Deposit')),
                ('fee_margin', models.DecimalField(blank=True, decimal_places=2, help_text='Rate charged as transaction fee for transactions performed on Account.', max_digits=300, null=True, verbose_name='Transaction Fee Margin')),
                ('interest_rate', models.DecimalField(blank=True, decimal_places=2, help_text='The interest rate of the Account type.', max_digits=300, null=True, verbose_name='Interest Rate')),
                ('auto_create', models.BooleanField(blank=True, default=False, help_text='Toggle auto-create to allow transactions performed on Account to be completed with or without approval.', null=True, verbose_name='Auto Create')),
                ('min_balance', models.DecimalField(blank=True, decimal_places=2, help_text='The minimum balance a Account. Without a Account holding a minimum balance, the Account will be rendered inactive.', max_digits=300, null=True, verbose_name='Min Balance')),
                ('max_deposit', models.DecimalField(blank=True, decimal_places=2, help_text='The maximum amount to deposit on a Account', max_digits=300, null=True, verbose_name='Max Deposit')),
                ('min_deposit', models.DecimalField(blank=True, decimal_places=2, help_text='The minimum amount to deposit on a Account', max_digits=300, null=True, verbose_name='Min Deposit')),
                ('max_withdrawal', models.DecimalField(blank=True, decimal_places=2, help_text='The maximum amount to withdrawal on a Account', max_digits=300, null=True, verbose_name='Max Withdrawal')),
                ('min_withdrawal', models.DecimalField(blank=True, decimal_places=2, help_text='The minimum amount to withdrawal on a Account', max_digits=300, null=True, verbose_name='Min Withdrawal')),
                ('allowed_currency', models.CharField(blank=True, help_text='The currencies allowed for Account funding.', max_length=250, null=True, verbose_name='Allowed Currency')),
            ],
            options={
                'verbose_name': 'Balance',
                'verbose_name_plural': 'Balance',
                'ordering': ('-created_date',),
            },
        ),
        migrations.CreateModel(
            name='Balance',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, help_text='The unique identifier of an object.', primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, editable=False, help_text='Timestamp when the record was created. The date and time \n            are displayed in the Timezone from where request is made. \n            e.g. 2019-14-29T00:15:09Z for April 29, 2019 0:15:09 UTC', verbose_name='Created')),
                ('modified_date', models.DateTimeField(auto_now=True, help_text='Timestamp when the record was modified. The date and \n            time are displayed in the Timezone from where request \n            is made. e.g. 2019-14-29T00:15:09Z for April 29, 2019 0:15:09 UTC\n            ', null=True, verbose_name='Updated')),
                ('value', models.DecimalField(blank=True, decimal_places=2, help_text='The unit value of the amount', max_digits=300, null=True, verbose_name='Value')),
                ('currency', models.CharField(blank=True, default='EUR', help_text='Three digit currency code. ISO 4217 e.g. EUR for Euro', max_length=3, null=True, verbose_name='Currency')),
            ],
            options={
                'verbose_name': 'Balance',
                'verbose_name_plural': 'Balance',
                'ordering': ('-created_date',),
            },
        ),
        migrations.CreateModel(
            name='BankAddress',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, help_text='The unique identifier of an object.', primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, editable=False, help_text='Timestamp when the record was created. The date and time \n            are displayed in the Timezone from where request is made. \n            e.g. 2019-14-29T00:15:09Z for April 29, 2019 0:15:09 UTC', verbose_name='Created')),
                ('modified_date', models.DateTimeField(auto_now=True, help_text='Timestamp when the record was modified. The date and \n            time are displayed in the Timezone from where request \n            is made. e.g. 2019-14-29T00:15:09Z for April 29, 2019 0:15:09 UTC\n            ', null=True, verbose_name='Updated')),
                ('country', models.CharField(blank=True, help_text='The two character ISO 3166-1 alpha-2 country code of the virtual account. ', max_length=3, null=True, verbose_name='Country')),
                ('deleted', models.DateTimeField(help_text='Timestamp when the record was deleted. The date and time \n            are displayed in the Timezone from where request is made. \n            e.g. 2019-14-29T00:15:09Z for April 29, 2019 0:15:09 UTC', verbose_name='Created')),
                ('address_line_1', models.CharField(blank=True, help_text='Address line 1: street, house, apartment. ', max_length=260, null=True, verbose_name='Address Line 1')),
                ('address_line_2', models.CharField(blank=True, help_text='Address line 2: street, house, apartment. ', max_length=260, null=True, verbose_name='Address Line 2')),
                ('state', models.CharField(blank=True, help_text='The State/Region/Province of the address.', max_length=260, null=True, verbose_name='State')),
                ('city', models.CharField(blank=True, help_text='The city of the address.', max_length=260, null=True, verbose_name='City')),
                ('zip_code', models.CharField(blank=True, help_text='The Zip code/Postal code of the address. Identifier consisting of a group of letters and/or numbers that is added to a postal address to assist the sorting of mail.', max_length=260, null=True, verbose_name='Zip Code')),
            ],
            options={
                'verbose_name': 'Bank Address',
                'verbose_name_plural': 'Bank Address',
                'ordering': ('-created_date',),
            },
        ),
        migrations.CreateModel(
            name='FundingAccounts',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, help_text='The unique identifier of an object.', primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, editable=False, help_text='Timestamp when the record was created. The date and time \n            are displayed in the Timezone from where request is made. \n            e.g. 2019-14-29T00:15:09Z for April 29, 2019 0:15:09 UTC', verbose_name='Created')),
                ('modified_date', models.DateTimeField(auto_now=True, help_text='Timestamp when the record was modified. The date and \n            time are displayed in the Timezone from where request \n            is made. e.g. 2019-14-29T00:15:09Z for April 29, 2019 0:15:09 UTC\n            ', null=True, verbose_name='Updated')),
                ('bank_name', models.CharField(blank=True, help_text='The name of the bank or financial institution', max_length=260, null=True, verbose_name='Bank Name')),
                ('payment_type', models.CharField(blank=True, choices=[('PRIORITY', 'PRIORITY'), ('REGULAR', 'REGULAR')], help_text='The shows the payment type when the payment will be initiated', max_length=20, null=True, verbose_name='Payment Type')),
                ('identifier_type', models.CharField(blank=True, choices=[('BIC_SWIFT', 'BIC_SWIFT'), ('SORT_CODE', 'SORT_CODE'), ('ROUTING_NUMBER', 'ROUTING_NUMBER'), ('ACH_ROUTING_NUMBER', 'ACH_ROUTING_NUMBER'), ('ROUTING_CODE', 'ROUTING_CODE'), ('WIRE_ROUTING_NUMBER', 'WIRE_ROUTING_NUMBER')], help_text='Depending on the payment type and country, Account code is represented by BIC/SWIFT codes, Bsb, Nsc, NSS or IFSC codes.', max_length=50, null=True, verbose_name='Identifier Type')),
                ('identifier_value', models.CharField(blank=True, help_text='The shows the payment type when the payment will be initiated', max_length=60, null=True, verbose_name='Identifier Value')),
                ('account_number_type', models.CharField(blank=True, choices=[('IBAN', 'IBAN'), ('ACCOUNT_NUMBER', 'ACCOUNT_NUMBER'), ('INTERNATIONAL', 'INTERNATIONAL')], help_text='The shows the account number type type when the payment will be initiated', max_length=30, null=True, verbose_name='Account Number Type')),
                ('account_number', models.CharField(blank=True, help_text='The shows the payment type when the payment will be initiated', max_length=60, null=True, verbose_name='Account Number')),
                ('funding_instructions', models.CharField(blank=True, help_text='Reference ID assigned by the bank that originated the transfer to the GenioPay Account', max_length=260, null=True, verbose_name='Funding Instructions')),
                ('supported_currencies', models.TextField(help_text='Array of currencies supported for the virtual account. Three-letter ISO 4217 code.', verbose_name='Supported Currencies')),
                ('bank_address', models.ForeignKey(blank=True, help_text='The shows the bank address', null=True, on_delete=django.db.models.deletion.CASCADE, to='transfer.bankaddress', verbose_name='Bank Address')),
            ],
            options={
                'verbose_name': 'Funding Accounts',
                'verbose_name_plural': 'Funding Accounts',
                'ordering': ('-created_date',),
            },
        ),
        migrations.CreateModel(
            name='BankAccount',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, help_text='The unique identifier of an object.', primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, editable=False, help_text='Timestamp when the record was created. The date and time \n            are displayed in the Timezone from where request is made. \n            e.g. 2019-14-29T00:15:09Z for April 29, 2019 0:15:09 UTC', verbose_name='Created')),
                ('modified_date', models.DateTimeField(auto_now=True, help_text='Timestamp when the record was modified. The date and \n            time are displayed in the Timezone from where request \n            is made. e.g. 2019-14-29T00:15:09Z for April 29, 2019 0:15:09 UTC\n            ', null=True, verbose_name='Updated')),
                ('account_id', models.UUIDField(blank=True, help_text='The unique identifier of the customer.', null=True, verbose_name='Account ID')),
                ('friendly_name', models.CharField(blank=True, help_text='A user friendly name set to identify a Account balance', max_length=20, null=True, verbose_name='Friendly Name')),
                ('currency', models.CharField(blank=True, help_text='Three digit currency code. ISO 4217 e.g. EUR for Euro.', max_length=3, null=True, verbose_name='Currency')),
                ('status', models.CharField(blank=True, help_text='The status of the Account.', max_length=20, null=True, verbose_name='Status')),
                ('requirements_type', models.CharField(blank=True, help_text='Requirements to fulfill to complete Account order.', max_length=100, null=True, verbose_name='Requirements Type')),
                ('requirements_status', models.CharField(blank=True, help_text='Requirement type status', max_length=20, null=True, verbose_name='Requirements Status')),
                ('default', models.BooleanField(blank=True, default=False, help_text='This defaults to False. Indicates whether Account is default account.', null=True, verbose_name='Default Account')),
                ('is_linked', models.BooleanField(blank=True, default=False, help_text='Defaults to False. If Account is imported from ASPSP connection', null=True, verbose_name='Is Linked')),
                ('has_account_details', models.BooleanField(blank=True, default=False, null=True, verbose_name='Has Account Details')),
                ('account_details', models.ForeignKey(blank=True, help_text='this store the account details for funding', max_length=20, null=True, on_delete=django.db.models.deletion.CASCADE, to='transfer.accountdetails', verbose_name='Account Details')),
                ('account_type', models.ForeignKey(blank=True, help_text='this stores the account type', max_length=20, null=True, on_delete=django.db.models.deletion.CASCADE, to='transfer.accounttype', verbose_name='Account Type')),
                ('available_balance', models.OneToOneField(blank=True, help_text="Funds that are at customers' disposal. Used e.g. for payment instruction acceptance. Includes bookings (positive ones scoped by valuta_date of current day or in the past, as well as negative bookings including dispositions - so independently of valuta_date), corrected on reservations (temporary funds blocks) and account limit.", null=True, on_delete=django.db.models.deletion.CASCADE, related_name='available_balance', to='transfer.balance', verbose_name='Available Balance')),
                ('blocked_balance', models.OneToOneField(blank=True, help_text='Blocked balance is an unsettled amount or payment. This may be an unsettled card transaction or a disputed transaction.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='blocked_balance', to='transfer.balance', verbose_name='Blocked Balance')),
                ('ledger_balance', models.OneToOneField(blank=True, help_text='Extended balance of the account including any pending transactions.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ledger_balance', to='transfer.balance', verbose_name='Ledger Balance')),
                ('pending_balance', models.OneToOneField(blank=True, help_text='The Pending balance of the Account', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pending_balance', to='transfer.balance', verbose_name='Pending Balance')),
                ('total_incoming', models.OneToOneField(blank=True, help_text='The total amount of funds received to the Account', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='total_incoming', to='transfer.balance', verbose_name='Total Incoming')),
                ('user', models.ForeignKey(help_text='The user for whom address belongs to', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User Profile')),
            ],
            options={
                'verbose_name': 'Bank Account',
                'verbose_name_plural': 'Bank Account',
                'ordering': ('-created_date',),
            },
        ),
        migrations.AddField(
            model_name='accountdetails',
            name='funding_accounts',
            field=models.ManyToManyField(help_text='The shows the funding accounts available', to='transfer.fundingaccounts', verbose_name='Funding Accounts'),
        ),
    ]