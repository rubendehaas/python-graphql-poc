from graphene import ObjectType, List, ID, Field
from graphene.relay import Node
from graphene_mongo import MongoengineConnectionField, MongoengineObjectType

from app.model.user_model import User as UserModel
from app.data.user.types import User as UserType

class Query(ObjectType):
    node = Node.Field()
    user = Field(UserType, userid=ID(required=False, default_value=None))
    users = List(UserType)

    def resolve_user(self, info, userid=None):
        return UserModel.objects(pk=userid).get()

    def resolve_users(self, info, userid=None):
        return list(UserModel.objects.all())