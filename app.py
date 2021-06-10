from flask import Flask, Blueprint
from flask_restful import Api
from flask_login import LoginManager
from db import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///wumboUsers.db'
db.init_app(app)
api = Api(app)

login_manager = LoginManager()
login_manager.init_app(app)

# from .models import User

# @login_manager.user_loader
# def load_user(user_id):
#     return User.get(user_id)

import resources.apiResouces as endpoint

api.add_resource(endpoint.Version, '/api')
api.add_resource(endpoint.AddTransaction, '/api/addTransaction')
api.add_resource(endpoint.ImportKey, '/api/ImportKey')
api.add_resource(endpoint.MakeKeys, '/api/MakeKeys')
api.add_resource(endpoint.GetBlock, '/api/getBlock/<int:blockNum>')
api.add_resource(endpoint.GetUser, '/api/getUser/<string:username>')
api.add_resource(endpoint.CreateUser, '/api/createUser')

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
