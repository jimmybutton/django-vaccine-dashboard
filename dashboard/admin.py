from django.contrib import admin

from .models import Entry

class EntryAdmin(admin.ModelAdmin):
    list_display = ["country", "date", "total_vaccinations", "total_vaccinations_per_hundred"]

admin.site.register(Entry, EntryAdmin)
