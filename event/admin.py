from django.contrib import admin
from .models import User, EventCategory, Event, EventMember, Contact, Suggestion

# Register your models here.
admin.site.register(User)
admin.site.register(Event)
admin.site.register(EventCategory)
admin.site.register(Contact)
admin.site.register(Suggestion)


# admin.site.register(Organizers)

@admin.register(EventMember)
class StudentUserAdmin(admin.ModelAdmin):
    list_display = EventMember.DisplayField
