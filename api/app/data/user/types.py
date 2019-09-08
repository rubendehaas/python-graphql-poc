import graphene
from graphene.relay import Node
from graphene_mongo import MongoengineObjectType

from app.model.user_model import User as UserModel

class User(MongoengineObjectType):

    class  Meta:
        model = UserModel
        interfaces = (Node,)
