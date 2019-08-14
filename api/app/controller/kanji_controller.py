from flask import Blueprint, jsonify

from graphene import ObjectType, Field, Schema

from app.schema.user_schema import schema

kanji = Blueprint('kanji', __name__)

@kanji.route('/kanji', methods=['GET'])
def index():

	result = schema.execute(
	    '''
	    {
		  user {
		    lastname
		  }
		}
	    '''
	)

	return jsonify(
		data=result.data
	)