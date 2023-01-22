import json
import sqlite3


with open('blockchain/current.wub', 'x') as f:
    json.dump(
        {   "header": {
            "blockID": 1,
            "creator": "wumbo",
            'prevBlockHash': "",
            "blockReward": 6,
            "proofOfWork": 0,
            "rewardReciever": "wumbo"
            },
            "transactions": {}
        },
        f)
    
con = sqlite3.connect("wumboUsers.db")
cur = con.cursor()

# start new block

# ? run flask server ?
# create admin user

