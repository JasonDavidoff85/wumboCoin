from typing import Text
from flask import jsonify, request, make_response
from flask_restful import Resource, reqparse
import flask_praetorian
from models import User
from db import db
from auth import guard
from common.wumbo import wumbo

class Authenticate(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('username', required=True, help='must include username')
        parser.add_argument('password', required=True, help='must include password')
        args = parser.parse_args()
        user = guard.authenticate(args['username'], args['password'])
        
        ret = {"access_token": guard.encode_jwt_token(user)}
        return make_response(jsonify(ret), 200)

class CreateUser(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('username', required=True, help='must include username')
        parser.add_argument('password', required=True, help='must include password')
        args = parser.parse_args()

        user = User.query.filter_by(username=args['username']).first()
        if user:
            return {'user already in database': True}

        # currently makes your key for you and stores private key in db. Might change
        wumboSession = wumbo()
        new_user = User(username=args['username'], passHash=guard.hash_password(args['password']), privKey=wumboSession.makeKeys(), balance=0)
        db.session.add(new_user)
        db.session.commit()
        loggedInUser = guard.authenticate(args['username'], args['password'])
        ret = {"access_token": guard.encode_jwt_token(loggedInUser)}
        return {"User {} created".format(args['username']): 400, "access_token": guard.encode_jwt_token(loggedInUser)}

class GetBlock(Resource):
    def get(self, blockNum):
        coin = wumbo()
        return coin.getBlock(blockNum)

class GetUser(Resource):
    def get(self, username):
        user = User.query.filter_by(username=username).first()
        if not user:
            return {"user not found": 401}
        wumboSession = wumbo(user.privKey)
        return {"username": user.username, "balance": user.balance, "public key": wumboSession.getPubKey()}

class Version(Resource):
    def get(self):
        return {'version': '0.1'}

class AddTransaction(Resource):
    @flask_praetorian.auth_required
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('receiver', required=True, help='must include receiver')
        parser.add_argument('amount', required=True, help='must include amount')
        args = parser.parse_args()
        
        #check if possible with db

        wumboSession = wumbo(flask_praetorian.current_user().privKey)
        username = flask_praetorian.current_user().username
        return wumboSession.giveCoins(username, args['receiver'], args['amount'])
        
        # if success update db

        return

# TODO look into options for importing pre existing keys
# and giving the option to make keys
'''
class ImportKey(Resource):
    @flask_praetorian.auth_required
    def post(self):
        json_data = request.get_json(force=True)
        # puts json data in db
        return

class MakeKeys(Resource):
    @flask_praetorian.auth_required
    def get(self):
        wumboSession = wumbo()
        flask_praetorian.current_user.privKey = wumboSession.makeKeys()
        session.commit()
        return
'''

