# Generated by Django 5.0.2 on 2024-03-01 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0020_remove_event_participants'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='event_category/'),
        ),
    ]
