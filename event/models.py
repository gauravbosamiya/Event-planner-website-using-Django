from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    name = models.CharField(max_length=100, null=True)
    email = models.EmailField(unique=True)
    bio = models.TextField(null=True, blank=True)
    heckathon_participant = models.BooleanField(default=True, null=True)
    type = models.CharField(max_length=15, null=True, blank=True, default='participant')
    # type = models.CharField(max_length=100, null=True, blank=True)
    avatar = models.ImageField(upload_to='event_category/', null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']


#
# class Organizers(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     mobile = models.CharField(max_length=15, null=False, blank=False)
#     image = models.FileField()
#     gender = models.CharField(max_length=15, null=False, blank=False)
#     type = models.CharField(max_length=15, null=False, blank=False)
#
#     def __str__(self):
#         return self.user.username


class EventCategory(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=6, unique=True)
    image = models.ImageField(upload_to='event_category/')
    created_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_user')
    updated_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='updated_user')
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now_add=True)
    status_choice = (
        ('disabled', 'Disabled'),
        ('active', 'Active'),
        ('deleted', 'Deleted'),
        ('blocked', 'Blocked'),
        ('completed', 'Completed'),
    )
    status = models.CharField(choices=status_choice, max_length=10)

    def __str__(self):
        return self.name


class Event(models.Model):
    category = models.ForeignKey(EventCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, unique=True)
    uid = models.PositiveIntegerField(unique=True)
    description = models.TextField()
    image = models.ImageField(upload_to='event_category/', null=True, blank=True)
    select_scheduled_status = (
        ('yet to scheduled', 'Yet to Scheduled'),
        ('scheduled', 'Scheduled')
    )
    scheduled_status = models.CharField(max_length=25, choices=select_scheduled_status)
    venue = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    created_user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True,
                                     related_name='event_created_user')
    updated_user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True,
                                     related_name='event_updated_user')
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now_add=True)
    status_choice = (
        ('disabled', 'Disabled'),
        ('active', 'Active'),
        ('deleted', 'Deleted'),
        ('time out', 'Time Out'),
        ('completed', 'Completed'),
        ('cancel', 'Cancel'),
    )
    status = models.CharField(choices=status_choice, max_length=10)

    participants = models.ManyToManyField(User, blank=True, related_name='events')

    def __str__(self):
        return self.name


class EventMember(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    attend_status_choice = (
        ('waiting', 'Waiting'),
        ('attending', 'Attending'),
        ('completed', 'Completed'),
        ('absent', 'Absent'),
        ('cancelled', 'Cancelled'),
    )
    # attend_status = models.CharField(choices=attend_status_choice, max_length=10)
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now_add=True)

    DisplayField = ['event', 'user']


class Contact(models.Model):
    email = models.ForeignKey(User, on_delete=models.CASCADE, related_name='contact_emails')
    subject = models.TextField(max_length=100)
    message = models.TextField(max_length=400)

    def __str__(self):
        return self.subject


class Suggestion(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    suggestion = models.TextField(max_length=500)

    def __str__(self):
        return self.event.name
