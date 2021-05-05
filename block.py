import random
class Block():
    def __init__(self, lastBlock):
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
        self.ledger[self.height] = {
            'transaction': transaction,
            'signature': signature,
            'key': pubKey.hex()
        }
        self.height += 1

    # returns dic of block
    def export(self, username):
        block = {
            'header': {
                'blockID': self.blockNum,
                'previousBlockHash': self.lastBlock,
                'username': username,
                'blockReward': self.blockReward,
                'proofOfWork': 0
            },
            'transactions': self.ledger
        }
        return block
     
    def blockHash():
        return

    def mineBlock(self):
        return