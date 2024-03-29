# Generated by Django 5.0.2 on 2024-02-24 17:49

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0003_eventcategory_delete_event'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('uid', models.PositiveIntegerField(unique=True)),
                ('description', models.TextField()),
                ('scheduled_status', models.CharField(choices=[('yet to scheduled', 'Yet to Scheduled'), ('scheduled', 'Scheduled')], max_length=25)),
                ('venue', models.CharField(max_length=255)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('created_date', models.DateField(auto_now_add=True)),
                ('updated_date', models.DateField(auto_now_add=True)),
                ('status', models.CharField(choices=[('disabled', 'Disabled'), ('active', 'Active'), ('deleted', 'Deleted'), ('time out', 'Time Out'), ('completed', 'Completed'), ('cancel', 'Cancel')], max_length=10)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.eventcategory')),
                ('created_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='event_created_user', to=settings.AUTH_USER_MODEL)),
                ('updated_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='event_updated_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
