from flask import jsonify, Blueprint

from flask.ext.restful import Resource, Api

import models


class cat(Resource):
    def get(self):
        return jsonify({'cat': [{'name': 'Python'}]})

class singlecat(Resource):
        def get(self, id):
            return jsonify({'name': 'Python'})

        def put(self, id):
            return jsonify({'name': 'Python'})

        def delete(self, id):
             return jsonify({'name': 'Python'})

cat_api = Blueprint('resources.cat', __name__)
api = Api(cat_api)
api.add_resource(
    cat,
    '/api/v1/cat',
    endpoint='cats'
)
api.add_resource(
     singlecat,
    '/api/v1/cat/<int:id>',
    endpoint='cat'
)
