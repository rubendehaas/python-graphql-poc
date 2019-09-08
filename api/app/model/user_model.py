from mongoengine import Document
from mongoengine.fields import StringField
import graphene

class User(Document):
    meta = {'collection': 'user'}

    firstname = StringField()
    lastname = StringField()