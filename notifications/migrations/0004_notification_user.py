# Generated by Django 4.1 on 2023-12-26 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0003_remove_notification_users'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='user',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
