from common.wumboCoin import wumboCoin

from common.wumboCrypt import Crypto;
import json
import requests

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

# resp = requests.post('http://127.0.0.1:5000/api/createUser', data={'username': 'Jason2', 'password': 'hunter2'}).json()
resp = requests.post('http://127.0.0.1:5000/api/authenticate', data={'username': 'Jason2', 'password': 'hunter2'}).json()
print(resp)
resp = requests.get('http://127.0.0.1:5000/api/getBlock/1').json()
print(resp)