import graphene

class User(graphene.ObjectType):
    id = graphene.ID()
    firstname = graphene.String()
    lastname = graphene.String()
    full_name = graphene.String()

    def resolve_full_name(self, info):
        return f"{self.firstname} {self.lastname}"

data = [
    User(id=1, firstname="Yuka", lastname="Sen"),
    User(id=2, firstname="Ruben", lastname="de Haas"),
]