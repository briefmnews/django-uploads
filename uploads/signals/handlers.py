import logging
import os

from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver

from uploads.models import Document

logger = logging.getLogger(__name__)


@receiver(pre_delete, sender=Document)
def delete_files(sender, instance, **kwargs):
    try:
        os.remove(instance.file.path)
    except FileNotFoundError:
        logger.info("The file was already deleted.")
