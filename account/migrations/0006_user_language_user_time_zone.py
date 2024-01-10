# Generated by Django 4.2.9 on 2024-01-09 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_rename_contact_number_user_mobile_user_accept_terms_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='language',
            field=models.CharField(blank=True, default='en', help_text='Customers language preference. All website communications will be sent out based on the users preferred language. ISO 639-1 code. Used as the language for notification emails sent by us. Defaults to the country code of the address or', max_length=3, null=True, verbose_name='Language'),
        ),
        migrations.AddField(
            model_name='user',
            name='time_zone',
            field=models.CharField(blank=True, default='Europe/London', help_text='The user Timezone is a client-specific Timezone that can be defined for the user time and user date of each individual user.', max_length=100, null=True, verbose_name='Time Zone'),
        ),
    ]
