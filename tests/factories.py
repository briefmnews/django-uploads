import factory

from uploads.models import Document


class DocumentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Document

    name = factory.Sequence(lambda n: "Document {0}".format(n))
    file = "fixtures/sample.pdf"
