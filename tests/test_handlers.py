import pytest

pytestmark = pytest.mark.django_db


class TestDeleteFiles:
    def test_with_existing_file(self, document, mocker):
        # GIVEN
        mock_remove = mocker.patch("os.remove")

        # WHEN
        document.delete()

        # THEN
        mock_remove.assert_called_once_with(document.file.path)

    def test_with_not_existing_file(self, document, mocker):
        # GIVEN
        mock_logger = mocker.patch("uploads.signals.handlers.logger.info")
        mock_remove = mocker.patch("os.remove", side_effect=FileNotFoundError)

        # WHEN
        document.delete()

        # THEN
        mock_remove.assert_called_once_with(document.file.path)
        mock_logger.assert_called_once_with("The file was already deleted.")

    def test_delete_large_image_file(self, large_image, mocker):
        # GIVEN
        mock_remove = mocker.patch("os.remove")

        # WHEN
        large_image.delete()

        # THEN
        mock_remove.assert_called_once_with(large_image.file.path)

    def test_delete_small_image_file(self, small_image, mocker):
        # GIVEN
        mock_remove = mocker.patch("os.remove")

        # WHEN
        small_image.delete()

        # THEN
        mock_remove.assert_called_once_with(small_image.file.path)
