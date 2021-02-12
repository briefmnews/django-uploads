from django.conf import settings
from django.contrib import admin
from django.utils.html import mark_safe

from .models import Document


class DocumentAdmin(admin.ModelAdmin):
    list_display = ("__str__", "description", "file_absolute_url", "updated")
    readonly_fields = ("updated", "created")

    def file_absolute_url(self, obj):
        url = f"{settings.SITE_DOMAIN}{obj.file.url}"
        return mark_safe(f"<a href='{url}' target='_BLANK'>File link</a>")


admin.site.register(Document, DocumentAdmin)
