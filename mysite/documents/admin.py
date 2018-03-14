from django.contrib import admin
from .models import newdoc

class DocAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,                      {"fields": ["title"]}),
        ("Date information",        {"fields": ["created_time"]}),
        (None,                      {"fields": ["modified_time"]}),
        ("Author information",      {"fields": ["author"]}),
        (None,                      {"fields": ["body"]})
   ]

    list_filter = ["created_time"]
    list_display = ('title', 'created_time', 'author')
    search_fields = ["title"]

#class uploaded(admin.ModelAdmin):

# Register models here.
admin.site.register(newdoc, DocAdmin)
