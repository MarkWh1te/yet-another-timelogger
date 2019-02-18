from django.contrib import admin
from record.models import Record


class AuthorAdmin(admin.ModelAdmin):
    pass


admin.site.register(Record, AuthorAdmin)
