# Generated by Django 4.1 on 2023-12-22 09:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0002_notification_category_notification_expiry_time_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notification',
            name='users',
        ),
    ]
