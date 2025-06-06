import pytest

from uploads.models import Document

pytestmark = pytest.mark.django_db


class TestDocument:
    def test_upload_file(self, document):
        assert document.pk == Document.objects.last().pk

    def test_rename_file_with_accent(self, document_with_accent):
        # GIVEN
        original_name = document_with_accent.name
        original_file_path = document_with_accent.file.path

        # WHEN
        document_with_accent.name = "Nouveau nom sans accent"
        document_with_accent.save(update_fields=['name'])

        # THEN
        assert document_with_accent.name == "Nouveau nom sans accent"
        assert document_with_accent.file.path != original_file_path
        assert not any(c in document_with_accent.name for c in "éèêëàâäôöûüç")

    def test_file_size_warning_for_large_image(self, large_image):
        # GIVEN
        size_in_mb = large_image.file.size / (1024 * 1024)

        # WHEN
        file_size_display = large_image.get_file_size()

        # THEN
        assert "Mo" in file_size_display
        assert "⚠️" in file_size_display
        assert str(round(size_in_mb, 2)) in file_size_display

    def test_file_size_no_warning_for_small_image(self, small_image):
        # GIVEN
        size_in_kb = small_image.file.size / 1024

        # WHEN
        file_size_display = small_image.get_file_size()

        # THEN
        assert "Ko" in file_size_display
        assert "⚠️" not in file_size_display
        assert str(round(size_in_kb, 2)) in file_size_display

    def test_is_image_method(self, small_image, document):
        # GIVEN
        image_document = small_image
        non_image_document = document

        # WHEN
        is_image_result = image_document.is_image()
        is_not_image_result = non_image_document.is_image()

        # THEN
        assert is_image_result is True
        assert is_not_image_result is False
