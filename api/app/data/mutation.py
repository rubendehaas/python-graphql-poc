from graphene import ObjectType, Field

class Mutations(ObjectType):
    create_user = CreateUser.Field()