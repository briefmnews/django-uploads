import pytest
from factory.django import DjangoModelFactory
from factory import Faker
from uploads.models import Document


class DocumentFactory(DjangoModelFactory):
    class Meta:
        model = Document

    name = Faker("word")
    description = Faker("text")


@pytest.fixture
def document(mocker):
    # GIVEN
    mock_file = mocker.MagicMock()
    mock_file.name = "document.pdf"
    mock_file.size = 51200  # 50KB
    mock_file.path = "/fake/path/document.pdf"
    mock_file.url = "/media/document.pdf"
    mock_file.read.return_value = b"fake content"
    mock_file.file = mock_file

    # WHEN
    document = DocumentFactory(name="Test Document")
    document.file = mock_file

    # THEN
    return document


@pytest.fixture
def large_image(mocker):
    # GIVEN
    mock_file = mocker.MagicMock()
    mock_file.name = "large_image.jpg"
    mock_file.size = 1048576  # 1MB
    mock_file.path = "/fake/path/large_image.jpg"
    mock_file.url = "/media/large_image.jpg"
    mock_file.read.return_value = b"fake content"
    mock_file.file = mock_file

    # WHEN
    document = DocumentFactory(name="Large Image")
    document.file = mock_file

    # THEN
    return document


@pytest.fixture
def small_image(mocker):
    # GIVEN
    mock_file = mocker.MagicMock()
    mock_file.name = "small_image.jpg"
    mock_file.size = 102400  # 100KB
    mock_file.path = "/fake/path/small_image.jpg"
    mock_file.url = "/media/small_image.jpg"
    mock_file.read.return_value = b"fake content"
    mock_file.file = mock_file

    # WHEN
    document = DocumentFactory(name="Small Image")
    document.file = mock_file

    # THEN
    return document


@pytest.fixture
def document_with_accent(mocker):
    # GIVEN
    original_path = "/fake/path/document.pdf"
    new_path = "/fake/path/document_with_accent.pdf"
    
    mock_file = mocker.MagicMock()
    mock_file.name = "document.pdf"
    mock_file.size = 51200  # 50KB
    mock_file.path = original_path
    mock_file.url = "/media/document.pdf"
    mock_file.read.return_value = b"fake content"
    mock_file.file = mock_file

    # WHEN
    document = DocumentFactory(name="Documenté avec accent")
    document.file = mock_file

    def save(*args, **kwargs):
        if "update_fields" in kwargs and "name" in kwargs["update_fields"]:
            mock_file.path = new_path

    document.save = save

    # THEN
    return document
