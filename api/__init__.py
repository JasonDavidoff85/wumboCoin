from flask import Flask
from flask_restful import Api
from .api import *

app = Flask(__name__)
api = Api(app)

api.add_resource(AddTransaction, '/api/addTransaction')
api.add_resource(ImportKey, '/api/ImportKey')
api.add_resource(MakeKeys, '/api/MakeKeys')
api.add_resource(GetBlock, '/api/getBlock/<int:blockNum>')
api.add_resource(GetUser, '/api/getUser/<string:username>')

if __name__ == '__main__':
    app.run(debug=True)
