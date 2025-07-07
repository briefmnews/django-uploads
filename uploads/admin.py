from django.conf import settings
from django.contrib import admin
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils.html import mark_safe

from .models import Document


class DocumentAdmin(admin.ModelAdmin):
    list_display = ("__str__", "description", "file_size", "file_absolute_url", "updated")
    readonly_fields = ("file_size_display", "updated", "created")
    ordering = ("-updated",)
    search_fields = ("name", "description")
    fieldsets = (
        (None, {
            'fields': ('name', 'description', 'file', 'file_size_display', 'updated', 'created')
        }),
    )

    def file_size_display(self, obj):
        if obj and obj.file.size >= settings.UPLOADS_WARNING_SIZE and obj.is_image():
            return (
                f"<div style='color:black;background:#fff3cd;padding:8px;'>"
                f"⚠️ Attention : Cette image fait {obj.get_file_size()}. Il est recommandé de ne pas dépasser {int(settings.UPLOADS_WARNING_SIZE / 1024.0)} Ko."
                f"</div>"
            )
        return f"{obj.get_file_size()}"
    file_size_display = mark_safe(file_size_display)
    file_size_display.short_description = "Taille du fichier"

    @admin.display(description="Taille du fichier")
    def file_size(self, obj):
        return obj.get_file_size()

    @admin.display(description="Lien du fichier")
    def file_absolute_url(self, obj):
        url = f"{settings.SITE_DOMAIN}{obj.file.url}"
        return mark_safe(f"<a href='{url}' target='_BLANK'>{obj.file.name.split('/')[-1]}</a>")


admin.site.register(Document, DocumentAdmin)
