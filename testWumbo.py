from wumboCoin import wumboCoin

from wumboCrypt import Crypto;
import json

crypto = Crypto()
crypto.importKey()

signature = crypto.sign(str({'sender': 'Wumbo', 'receiver': 'Hannah & Joey', 'amount': 6}))

# print(signature.hex())

# print(crypto.getPubKey())

pubKey = 'MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAsXbeJN6YlJEeHJLFgVHsnPNK8GMO1SHtzbpzEkHXgATnelGqTzzWkHozLR8X4Q9HSEXxtQpujqSPxAUiaCAA1sG8c8oywjuolAHlJJPYGknpjI9J4lr8mY+MBNkA3TPR0if5McPXBfyhnYLH0ZinTuCNaJyiDIEJXqil0xshLVPc/HlrScAV0wUkcSkOTJsG+kHJ6pANy4YA2YyHcAHXVIkKquoRsbjBugrdOBqmpRbHFyVIWPiTswu2THThMiHDOtrdOytx5NC1NXxEaWC2dG+fOFD8C8tIGpPZUwTMh7Bd520JeBjJ6HoIoGQDzzmcEOIo4jPlvxn1vBAUe9uEkwIDAQAB'
genesis = {
    'header': {
        'blockID': 0,
        'username': "jdavidoff",
        'blockReward': 6,
        'proofOfWork': 0
    },
    'transactions': {
        0: {
            'transaction': {'sender': 'Wumbo', 'receiver': 'HannahJoeyPurvis', 'amount': 6},
            'signature': crypto.sign(str({'sender': 'Wumbo', 'receiver': 'HannahJoeyPurvis', 'amount': 6})).hex(),
            'key': pubKey
        },
        1: {
            'transaction': {'sender': 'Wumbo', 'receiver': 'Theydra', 'amount': 5},
            'signature': crypto.sign(str({'sender': 'Wumbo', 'receiver': 'Theydra', 'amount': 5})).hex(),
            'key': pubKey
        },
        2: {
            'transaction': {'sender': 'Wumbo', 'receiver': 'JohnPaolaEly', 'amount': 4},
            'signature': crypto.sign(str({'sender': 'Wumbo', 'receiver': 'JohnPaolaEly', 'amount': 4})).hex(),
            'key': pubKey
        },
        3: {
            'transaction': {'sender': 'Wumbo', 'receiver': 'NickD', 'amount': 2},
            'signature': crypto.sign(str({'sender': 'Wumbo', 'receiver': 'NickD', 'amount': 2})).hex(),
            'key': pubKey
        },
    }
}

with open('blockchain/genesis.wub', 'w') as f:
    json.dump(genesis, f)