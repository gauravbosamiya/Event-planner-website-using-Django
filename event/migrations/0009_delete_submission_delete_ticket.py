# Generated by Django 5.0.2 on 2024-03-01 02:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0008_submission_alter_event_participants_ticket'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Submission',
        ),
        migrations.DeleteModel(
            name='Ticket',
        ),
    ]
