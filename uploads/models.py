import logging

from django.core.exceptions import ObjectDoesNotExist
from django.core.files.base import ContentFile
from django.db import models

logger = logging.getLogger(__name__)


def upload_to(instance, filename):
    subdirectory = instance.subdirectory_path
    file_base = instance.name
    file_extension = filename.rsplit(".", 1)[1]
    return "{}{}.{}".format(subdirectory, file_base, file_extension)


class RenameMixin(models.Model):
    def save(self, *args, **kwargs):
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
