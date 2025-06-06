import logging
import unicodedata

from django.core.exceptions import ObjectDoesNotExist
from django.core.files.base import ContentFile
from django.db import models
from django.conf import settings

logger = logging.getLogger(__name__)


def upload_to(instance, filename):
    subdirectory = instance.subdirectory_path
    file_base = instance.name
    file_extension = filename.rsplit(".", 1)[1]
    return "{}{}.{}".format(subdirectory, file_base, file_extension)


class RenameMixin(models.Model):
    def save(self, *args, **kwargs):
        self.name = "".join(
            c for c in unicodedata.normalize("NFD", self.name)
            if unicodedata.category(c) != "Mn"
        )
        saved_object = self.get_saved_object()
        if saved_object is not None:
            if self.name != saved_object.name:
                if not self.file_deleted:
                    old_file = saved_object.file
                    new_file = ContentFile(old_file.read())
                    new_file.name = old_file.name
                    old_file.delete(False)
                    self.file = new_file
        super().save(*args, **kwargs)

    class Meta:
        abstract = True


class Document(RenameMixin, models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(null=True, blank=True)
    file = models.FileField(upload_to=upload_to)

    subdirectory_path = "documents/public/"

    def __str__(self):
        return self.name

    def get_saved_object(self):
        try:
            saved_object = self.__class__.objects.get(pk=self.pk)
        except ObjectDoesNotExist:
            saved_object = None

        return saved_object

    def save(self, *args, **kwargs):
        saved_object = self.get_saved_object()
        self.file_deleted = False

        if saved_object is not None:
            if getattr(self, "file") != getattr(saved_object, "file"):
                getattr(saved_object, "file").delete(False)
                self.file_deleted = True

        super().save(*args, **kwargs)

    def get_file_size(self):
        size = self.file.size
        warning = ""
        if size >= settings.UPLOADS_WARNING_SIZE and self.is_image(): 
            warning = "⚠️"

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

    def is_image(self):
        return self.file.name.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.webp'))
