# Generated by Django 5.0.2 on 2024-03-01 05:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0011_remove_eventmember_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eventmember',
            name='attend_status',
        ),
    ]
