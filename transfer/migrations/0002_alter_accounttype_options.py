# Generated by Django 4.2.9 on 2024-01-13 14:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transfer', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='accounttype',
            options={'ordering': ('-created_date',), 'verbose_name': 'Bank Account Type', 'verbose_name_plural': 'Bank Account Type'},
        ),
    ]
