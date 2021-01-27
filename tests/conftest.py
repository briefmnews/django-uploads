import pytest

from .factories import DocumentFactory


@pytest.fixture
def document():
    return DocumentFactory()
