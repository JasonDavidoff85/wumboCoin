from flask import Flask, Blueprint
from flask_restful import Api
import flask_cors
from db import db
from auth import guard
from models import Blockchain

cors = flask_cors.CORS()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///wumbo.db'
app.config["JWT_ACCESS_LIFESPAN"] = {"hours": 24}
app.config["JWT_REFRESH_LIFESPAN"] = {"days": 30}
app.config["CLEAN_RUN"] = False
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
api.add_resource(endpoint.GetLatest, '/api/getBlock')
api.add_resource(endpoint.GetUser, '/api/getUser/<string:username>')
api.add_resource(endpoint.CreateUser, '/api/createUser')
api.add_resource(endpoint.MineBlock, '/api/mineblock')

with app.app_context():
    db.create_all()
    if app.config["CLEAN_RUN"]:
        db.session.add(Blockchain(wub_file='./blockchain/genesis.wub', current=False, blockHash="00000055099ce9aeedb9ce2238817a28e2afd037d52b3292f511efc03bb80138"))
        db.session.add(Blockchain(wub_file='./blockchain/1.wub', current=True, prevBlockHash="00000055099ce9aeedb9ce2238817a28e2afd037d52b3292f511efc03bb80138"))
        db.session.commit()

if __name__ == '__main__':
    app.run(debug=True)
