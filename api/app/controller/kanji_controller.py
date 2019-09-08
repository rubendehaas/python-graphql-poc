from flask import Blueprint, jsonify, request
from flask_graphql import GraphQLView
from graphene import ObjectType, Field, Schema

from app.data.user.queries import Query as UserQuery
from app.data.user.mutations import Mutations as UserMutations
from app.data.user.types import User as UserType

kanji = Blueprint('kanji', __name__)
  
kanji.add_url_rule(
    '/graphql',
    view_func = GraphQLView.as_view(
        'graphql',
        schema = Schema(query=UserQuery, mutation=UserMutations, types=[UserType]),
        # schema = Schema(query=UserQuery, types=[UserType]),
        graphiql = True
    )
)