import graphene
from app.model.user_model import User as UserModel

class Query(graphene.ObjectType):
    user = graphene.Field(UserModel)
    def resolve_user(self, info):
    	return UserModel(id=1, firstname="Pjotr", lastname="Johannson")

schema = graphene.Schema(query=Query)