from django.conf import settings
from django.contrib import admin
from django.utils.html import mark_safe
from django.contrib import messages

from .models import Document


class DocumentAdmin(admin.ModelAdmin):
    list_display = ("__str__", "description", "get_file_size", "file_absolute_url", "updated")
    readonly_fields = ("updated", "created")
    ordering = ("-updated",)
    search_fields = ("name", "description", "get_file_size")

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        if obj and obj.file.size >= settings.UPLOADS_WARNING_SIZE and self.is_image(obj):
            if not hasattr(request, '_document_size_warning'):
                messages.warning(
                    request,
                    f"Attention : Cette image fait {self.get_file_size(obj)}. Il est recommandé de ne pas dépasser {int(settings.UPLOADS_WARNING_SIZE / 1024.0)} Ko."
                )
                request._document_size_warning = True
        return form

    @admin.display(
        description="Taille du fichier",
    )
    def get_file_size(self, obj):
        size = obj.file.size
        warning = ""
        if size >= settings.UPLOADS_WARNING_SIZE and self.is_image(obj): warning = "⚠️"

        if size < 512000:
            size = size / 1024.0
            ext = 'Ko'
        elif size < 4194304000:
            size = size / 1048576.0
            ext = 'Mo'
        else:
            size = size / 1073741824.0
            ext = 'Go'

        return f"{str(round(size, 2))} {ext} {warning}"
    
    def is_image(self, obj):
        return obj.file.name.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.webp'))

    @admin.display(description="Lien du fichier")
    def file_absolute_url(self, obj):
        url = f"{settings.SITE_DOMAIN}{obj.file.url}"
        return mark_safe(f"<a href='{url}' target='_BLANK'>{obj.file.name.split('/')[-1]}</a>")


admin.site.register(Document, DocumentAdmin)
