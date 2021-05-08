from flask import jsonify, request
from flask_restful import Resource
from wumboCoin import wumboCoin

class AddTransaction(Resource):
    def post(self):
        json_data = request.get_json(force=True)
        # call on wumbo coin
        # puts json data in db

class ImportKey(Resource):
    def post(self):
        json_data = request.get_json(force=True)
        # puts json data in db 

class MakeKeys(Resource):
    def get(self):
        # return key from db
        return

class GetBlock(Resource):
    def get(self, blockNum):
        return  # block id from db

class GetUser(Resource):
    def get(self, username):
        return #info on user from db


