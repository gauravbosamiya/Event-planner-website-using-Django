# Generated by Django 5.0.2 on 2024-03-01 19:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0018_alter_user_type_eventmember'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Organizers',
        ),
    ]