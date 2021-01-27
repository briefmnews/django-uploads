import pytest

from uploads.models import Document

pytestmark = pytest.mark.django_db


class TestDocument:
    def test_upload_file(self, document):
        assert document.pk == Document.objects.last().pk
