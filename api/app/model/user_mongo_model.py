from datetime import datetime
from mongoengine import Document, EmbeddedDocument
from mongoengine.fields import (
    DateTimeField, EmbeddedDocumentField,
    ListField, ReferenceField, StringField,
)

class User(Document):
    meta = {'collection': 'user'}

    firstname = StringField()
    lastname = StringField()