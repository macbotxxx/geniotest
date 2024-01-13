# Generated by Django 4.2.9 on 2024-01-12 00:16

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0010_user_geniopay_key_user_geniopay_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='geniopay_user_id',
            field=models.UUIDField(default=uuid.uuid4, help_text='GenioPay user ID is the unique identifier of the instance this object belongs to. Mandatory, unless a new instance to create is given.', verbose_name='GenioPay User ID'),
        ),
    ]
