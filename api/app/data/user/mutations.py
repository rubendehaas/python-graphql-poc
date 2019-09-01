from graphene import ObjectType, Field
import app.data.user.types as UserTypes

class Mutations(ObjectType):
    create_user = UserTypes.CreateUser.Field()
    update_user = UserTypes.UpdateUser.Field()
    delete_user = UserTypes.DeleteUser.Field()