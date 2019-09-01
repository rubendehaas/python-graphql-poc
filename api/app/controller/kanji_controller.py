from flask import Blueprint, jsonify, request
from flask_graphql import GraphQLView

from graphene import ObjectType, Field, Schema
from app.data.user.queries import Query as UserQuery
from app.data.user.mutations import Mutations as UserMutations

kanji = Blueprint('kanji', __name__)

kanji.add_url_rule(
    '/graphql',
    view_func = GraphQLView.as_view(
        'graphql',
        schema = Schema(query=UserQuery, mutation=UserMutations),
        graphiql = True
    )
)