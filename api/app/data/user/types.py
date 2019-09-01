import graphene
from app.model.user_model import data as UserData, User as UserModel

class CreateUserInput(graphene.InputObjectType):
    firstname = graphene.String()
    lastname = graphene.String()

class CreateUser(graphene.Mutation):
    user = graphene.Field(lambda: UserModel)

    class Arguments:
        user_data = CreateUserInput(required=True)

    def mutate(self, info, user_data=None):
        user = UserModel(**user_data)
        UserData.append(user)
        return CreateUser(user=user)

class UpdateUserInput(graphene.InputObjectType):
    id = graphene.Int()
    firstname = graphene.String()
    lastname = graphene.String()

class UpdateUser(graphene.Mutation):
    user = graphene.Field(lambda: UserModel)

    class Arguments:
        user_data = UpdateUserInput(required=True)

    def mutate(self, info, user_data=None):
        output = None
        target = None

        for index,user in enumerate(UserData):
            if user.id == user_data["id"]:
                target = index
                break

        if target != None:
            output = UserModel(**user_data)
            UserData[target] = output

        return UpdateUser(user=output)

class DeleteUserInput(graphene.InputObjectType):
    id = graphene.Int()

class DeleteUser(graphene.Mutation):
    user = graphene.Field(lambda: UserModel)

    class Arguments:
        user_data = DeleteUserInput(required=True)

    def mutate(self, info, user_data=None):
        output = None

        for index,user in enumerate(UserData):
            if user.id == user_data["id"]:
                target = index
                break

        if target != None:
            output = UserData.pop(target)

        return UpdateUser(user=output)