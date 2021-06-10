from typing import Text
from flask import jsonify, request
from flask_restful import Resource, reqparse
from flask_login import login_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from models import User
from db import db

class Authenticate(Resource):
    def post(self):

        login_user(user, remember=remember)
        return

class CreateUser(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('username', required=True, help='must include username')
        parser.add_argument('password', required=True, help='must include hashed password')
        args = parser.parse_args()

        user = User.query.filter_by(username=args['username']).first()
        if user:
            return {'user already in database': True}

        new_user = User(username=args['username'], passHash=args['password'], pubKey=None, balance=0)
        db.session.add(new_user)
        db.session.commit()
        return {"User: {} created".format(args['username']): True}

class GetBlock(Resource):
    def get(self, blockNum):
        return  # block id from db

class GetUser(Resource):
    def get(self, username):
        return #info on user from db

class Version(Resource):
    def get(self):
        return {'version': '0.1'}



class AddTransaction(Resource):
    @login_required
    def post(self):
        json_data = request.get_json(force=True)
        # call on wumbo coin

        # puts json data in db
        return
        # return dic of status message (ex status code)

class ImportKey(Resource):
    @login_required
    def post(self):
        json_data = request.get_json(force=True)
        # puts json data in db
        return

class MakeKeys(Resource):
    @login_required
    def get(self):
        # return key from db
        return

