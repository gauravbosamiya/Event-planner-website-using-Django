# Generated by Django 5.0.2 on 2024-02-24 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0006_alter_event_participants'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='heckathon_participant',
            field=models.BooleanField(default=True, null=True),
        ),
    ]