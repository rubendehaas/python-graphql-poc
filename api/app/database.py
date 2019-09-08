from mongoengine import connect

from app.model.user_model import User

connect('test', host="mongodb://mongo", alias='default')


def init_db():

    # Create the fixtures
    user1 = User(
        firstname = 'Pjotr',
        lastname = 'Johannson'
    )
    user1.save()

    user2 = User(
        firstname = 'Peter',
        lastname = 'Hanson'
    )
    user2.save()

    user3 = User(
        firstname = 'Paul',
        lastname = 'Fredrikson'
    )
    user3.save()
