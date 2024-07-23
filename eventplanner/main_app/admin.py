from django.contrib import admin

from .models import Event, Moment, Asset

# Register your models here.
admin.site.register(Event)
admin.site.register(Moment)
admin.site.register(Asset)