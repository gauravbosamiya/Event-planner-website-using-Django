# Generated by Django 5.0.2 on 2024-03-02 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0022_event_participants'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='event_category/'),
        ),
    ]
