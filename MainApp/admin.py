from django.contrib import admin

# Register your models here.
from .models import Entry
from .models import Topic

admin.site.register(Topic)
admin.site.register(Entry)
