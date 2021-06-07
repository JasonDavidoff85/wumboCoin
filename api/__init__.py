from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
import api as endpoint

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///wumboUsers.db'
api = Api(app)
db = SQLAlchemy(app)

api.add_resource(endpoint.Version, '/api')
api.add_resource(endpoint.AddTransaction, '/api/addTransaction')
api.add_resource(endpoint.ImportKey, '/api/ImportKey')
api.add_resource(endpoint.MakeKeys, '/api/MakeKeys')
api.add_resource(endpoint.GetBlock, '/api/getBlock/<int:blockNum>')
api.add_resource(endpoint.GetUser, '/api/getUser/<string:username>')

if __name__ == '__main__':
    app.run(debug=True)
