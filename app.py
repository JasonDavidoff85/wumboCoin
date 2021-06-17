from flask import Flask, Blueprint
from flask_restful import Api
import flask_cors
from db import db
from auth import guard

cors = flask_cors.CORS()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///wumboUsers.db'
app.config["JWT_ACCESS_LIFESPAN"] = {"hours": 24}
app.config["JWT_REFRESH_LIFESPAN"] = {"days": 30}
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
db.init_app(app)
api = Api(app)

from models import User

guard.init_app(app, User)
cors.init_app(app)

import resources.apiResouces as endpoint

api.add_resource(endpoint.Version, '/api')
api.add_resource(endpoint.Authenticate, '/api/authenticate')
api.add_resource(endpoint.AddTransaction, '/api/addTransaction')
api.add_resource(endpoint.GetBlock, '/api/getBlock/<string:blockNum>')
api.add_resource(endpoint.GetUser, '/api/getUser/<string:username>')
api.add_resource(endpoint.CreateUser, '/api/createUser')

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
