import pytest

pytestmark = pytest.mark.django_db


class TestDeleteFiles:
    def test_with_existing_file(self, document, mocker):
        # GIVEN
        mock = mocker.patch("os.remove")

        # WHEN
        document.delete()

        # THEN
        mock.assert_called_once_with(document.file.path)

    def test_with_not_existing_file(self, document, mocker):
        # GIVEN
        mock = mocker.patch("uploads.signals.handlers.logger.info")

        # WHEN
        document.delete()

        # THEN
        mock.assert_called_once_with("The file was already deleted.")
