from typing import Text
from flask import jsonify, request, make_response
from flask_restful import Resource, reqparse
import flask_praetorian
from models import User
from db import db
from auth import guard

class Authenticate(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('username', required=True, help='must include username')
        parser.add_argument('password', required=True, help='must include password')
        args = parser.parse_args()
        user = guard.authenticate(args['username'], args['password'])
        # user = User.query.filter_by(username=args['username']).first()
        # if not user:
        #     return {"Inncorrect username or password"}
        ret = {"access_token": guard.encode_jwt_token(user)}
        return make_response(jsonify(ret), 200)

class CreateUser(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('username', required=True, help='must include username')
        parser.add_argument('password', required=True, help='must include password')
        args = parser.parse_args()

        user = User.query.filter_by(username=args['username'].lower()).first()
        if user:
            return {'user already in database': True}

        new_user = User(username=args['username'], passHash=guard.hash_password(args['password']), pubKey=None, balance=0)
        db.session.add(new_user)
        db.session.commit()
        return {"User: {} created".format(args['username']): True}

class GetBlock(Resource):
    @flask_praetorian.auth_required
    def get(self, blockNum):
        return {"block id:": blockNum}

class GetUser(Resource):
    def get(self, username):
        print(username)
        user = User.query.filter_by(username=username).first()
        return user

class Version(Resource):
    def get(self):
        return {'version': '0.1'}


class AddTransaction(Resource):
    @flask_praetorian.auth_required
    def post(self):
        json_data = request.get_json(force=True)
        # call on wumbo coin

        # puts json data in db
        return
        # return dic of status message (ex status code)

class ImportKey(Resource):
    @flask_praetorian.auth_required
    def post(self):
        json_data = request.get_json(force=True)
        # puts json data in db
        return

class MakeKeys(Resource):
    @flask_praetorian.auth_required
    def get(self):
        # return key from db
        return

