
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256
from Crypto.Signature import pkcs1_15

from common.wumboCrypt import Crypto;
import json
import requests
from requests.structures import CaseInsensitiveDict
# crypto = Crypto()
# crypto.createKeyPair()

# #signature = crypto.sign(str({'sender': 'Wumbo', 'receiver': 'Hannah & Joey', 'amount': 6}))

# # print(signature.hex())

# # print(crypto.getPubKey())

# genesis = {
#     'header': {
#         'blockID': 0,
#         'creator': "jdavidoff",
#         'blockReward': 6,
#         'proofOfWork': 0,
#         'rewardReciever': "jdavidoff"
#     },
#     'transactions': {
#         0: {
#             'transaction': {'sender': 'Wumbo', 'receiver': 'HannahJoeyPurvis', 'amount': 6},
#             'signature': crypto.sign(str({'height': 0, 'sender': 'Wumbo', 'receiver': 'HannahJoeyPurvis', 'amount': 6})).hex()[:64]
#         },
#         1: {
#             'transaction': {'sender': 'Wumbo', 'receiver': 'Theydra', 'amount': 5},
#             'signature': crypto.sign(str({'height': 1, 'sender': 'Wumbo', 'receiver': 'Theydra', 'amount': 5})).hex()[:64]
#         },
#         2: {
#             'transaction': {'sender': 'Wumbo', 'receiver': 'JohnPaolaEly', 'amount': 4},
#             'signature': crypto.sign(str({'height': 2, 'sender': 'Wumbo', 'receiver': 'JohnPaolaEly', 'amount': 4})).hex()[:64]
#         },
#         3: {
#             'transaction': {'sender': 'Wumbo', 'receiver': 'NickD', 'amount': 2},
#             'signature': crypto.sign(str({'height': 3, 'sender': 'Wumbo', 'receiver': 'NickD', 'amount': 2})).hex()[:64]
#         },
#     }
# }

# with open('blockchain/genesis.wub', 'w') as f:
#     json.dump(genesis, f)

headers = CaseInsensitiveDict()
headers["Accept"] = "application/json"
headers["Authorization"] = "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE2MjM5NDEwNDUsImV4cCI6MTYyNDAyNzQ0NSwianRpIjoiZjVlYzIyMjItMTViMy00ZmUzLTk1ZTUtZjE0YmY0Njc5ZGMxIiwiaWQiOjEsInJscyI6IiIsInJmX2V4cCI6MTYyNjUzMzA0NX0.MJJ5i96ahAkuIyC9uN27VGuv04e47inu3ZWw81iEbIs"
# resp = requests.post('http://127.0.0.1:5000/api/addTransaction', headers=headers, data={"receiver": "Hannah", "amount": "1"}).json()
resp = requests.get('http://127.0.0.1:5000/api/getUser/wumbo', headers=headers).json()

# import public key
pubkey = RSA.import_key(resp['public key'])

# get block
resp = requests.get('http://127.0.0.1:5000/api/getBlock', headers=headers).json()
print(resp)

# get signature and convert to bytes
signature = bytes.fromhex(resp['transactions']['0']['signature'])
del resp['transactions']['0']['signature']

# isolate transaction be like what is hased
transaction = resp['transactions']
print(transaction)

# create hash of transaction
hashObj = SHA256.new(data=json.dumps(transaction).encode('utf-8'))

# verify hash with signature
try:
    pkcs1_15.new(pubkey).verify(hashObj, signature)
    print("valid")
except (ValueError, TypeError):
    print("invalid")

# signature = resp['transactions']["3"]["signature"]
# name = resp['transactions']["3"]['transaction']["sender"]
# transaction = resp['transactions']["3"]['transaction']
# resp = requests.get('http://127.0.0.1:5000/api/getUser/{}'.format(name), headers=headers).json()
# key = resp['public key']



# transaction = {
#     "0": {
#         "transaction": {
#             "sender": "Wumbo",
#             "receiver": "HannahJoeyPurvis",
#             "amount": 6
#         }
#     }
# }
# ########################################
# # this works. This is the crypto method
# priKey = RSA.generate(1024)
# print(transaction)
# hashObj = SHA256.new(data=json.dumps(transaction).encode('utf-8'))
# signature = pkcs1_15.new(priKey).sign(hashObj)

# pubKey = priKey.public_key()

# try:
#     pkcs1_15.new(pubKey).verify(hashObj, signature)
#     print("valid")
# except (ValueError, TypeError):
#     print("invalid")
# ########################################
