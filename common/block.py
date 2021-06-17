import random
import json
import os
# from wumboCoin import wumboCoin

class Block():
    def __init__(self, session, file=None):
        self.data = {}
        self.session = session
        if file != None and os.path.exists(file): # block already created
            with open(file) as f:
                self.data = json.load(f)
        self.height = len(self.data['transactions'])
        
    def calculateBlockReward(self):
        chance = []
        for i in range(15):
            chance[i].append(1)
        for i in range(8):
            chance[i].append(2)
        for i in range(6):
            chance[i].append(3)
        for i in range(4):
            chance[i].append(4)
        for i in range(2):
            chance[i].append(5)
        chance[i].append(6)

        return random.choice(chance)


    def addTransaction(self, transaction):
        toBeSigned = str({self.height: transaction})
        signature = self.session.crypto.sign(toBeSigned)
        self.data['transactions'][self.height] = {
            'transaction': transaction,
            'signature': signature.hex()
        }
        with open('blockchain/current.wub', 'w') as f:
            json.dump(self.data, f)
        self.height += 1
        return self.data['transactions'][self.height-1]

    
    def createNextBlock(self):
        newBlock = {}
        newBlock['header'] = {
            'blockID': self.data['header']['blockID'] + 1,
            'creator': self.session.username,
            'prevBlockHash': "", #TODO <-----------------------+
            'blockReward': self.calculateBlockReward(),
            'proofOfWork': 0,
            'rewardReciever': ""
        }
        newBlock['transactions'] = {}

        os.rename('blockchain/current.wub', 'blockchain/' + self.data['header']['blockID'] + '.wub')
        with open('blockchain/current.wub', 'w') as f:
            json.dump(newBlock, f)
        
        # may not work. look into
        self.data = newBlock

    def blockHash():
        return
