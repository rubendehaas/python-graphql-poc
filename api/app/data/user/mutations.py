import graphene

from app.model.user_model import User as UserModel
from app.data.user.types import User as UserType

class CreateUserInput(graphene.InputObjectType):
    firstname = graphene.String()
    lastname = graphene.String()

class CreateUser(graphene.Mutation):
    user = graphene.Field(lambda: UserType)

    class Arguments:
        user_data = CreateUserInput(required=True)

    def mutate(self, info, user_data=None):
        user = UserModel(**user_data)
        user.save(force_insert=True)
        return CreateUser(user=user)

class UpdateUserInput(graphene.InputObjectType):
    user_id = graphene.String()
    firstname = graphene.String()
    lastname = graphene.String()

class UpdateUser(graphene.Mutation):
    user = graphene.Field(lambda: UserType)

    class Arguments:
        user_data = UpdateUserInput(required=True)

    def mutate(self, info, user_data):
        user = UserModel.objects(pk=user_data.user_id).get()
        user.firstname = user_data.firstname
        user.lastname = user_data.lastname
        user.save()
        return UpdateUser(user=user)

class DeleteUserInput(graphene.InputObjectType):
    user_id = graphene.String()

class DeleteUser(graphene.Mutation):
    user = graphene.Field(lambda: UserType)

    class Arguments:
        user_data = DeleteUserInput(required=True)

    def mutate(self, info, user_data):
        user = UserModel.objects(pk=user_data.user_id).get()
        user.delete()
        return DeleteUser(user=user)

class Mutations(graphene.ObjectType):
    create_user = CreateUser.Field()
    update_user = UpdateUser.Field()
    delete_user = DeleteUser.Field()