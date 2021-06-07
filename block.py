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

            # get info from previous block:
            #	hash of previous block
            #	height of next transaction
            #
            self.blockNum = lastBlock.blockNum + 1
            self.prevBlock = lastBlock
            self.height = lastBlock.height
            self.prevHeight = lastBlock.height
            self.blockReward = self.calculateBlockReward()
            self.maxHeight = 3500 # TODO figure out # transactions to make 1MB block
            self.ledger = {}
            self.pOfw = 0
        
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


    def addTransaction(self, transaction, pubKey):
        signature = self.crypto.sign(str(transaction))
        self.data['transactions'][self.height] = {
            'transaction': transaction,
            'signature': signature,
            'key': pubKey.hex()
        }
        self.height += 1

    
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
        
        # either do this if possible
        self.session.block = self

        # or have callback to change wumboCoin session current block
        

     
    def blockHash():
        return
