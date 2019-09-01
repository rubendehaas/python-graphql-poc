from graphene import ObjectType, List, ID
from app.model.user_model import data as UserData, User as UserModel

class Query(ObjectType):
    users = List(UserModel, userid=ID(required=False, default_value=None))

    def resolve_users(
        self, 
        info, 
        userid=None,
        ):

        if userid is None:
            return UserData

        for user in UserData:
            if user.id is int(userid):
                return [user]