import json
import os
from .wumboCrypt import Crypto
from common.block import Block
#import gnupg

# transaction:
# 	id:
# 	sender:
# 	receiver:
# 	amount:
# sender key
# transaction signature

class wumbo():
	def __init__(self, privKey=None):
		self.crypto = Crypto(privKey)
		# set current block
		# TODO BUG have some sort of alias or protocol for current 
		# incase one isnt named that
		self.block = Block(self, 'blockchain/current.wub')
		
	def importKey(self, path):
		self.crypto.importKey(path)
	
	def makeKeys(self):
		return self.crypto.createKey()

	def giveCoins(self, sender, receiver, amount):
		transaction = {'sender': sender, 'receiver': receiver, 'amount': amount}
		return self.block.addTransaction(transaction)

	def getBlock(self, blockNum):
		blocks = os.listdir('blockchain/')

		files = {i.split(".")[0]: i for i in blocks}
		files.setdefault(blockNum, None)
		if files[blockNum] == None:
			return {"block not found": True}

		with open('blockchain/{}'.format(files[blockNum]), 'r') as f:
			blockData = json.load(f)
		
		return blockData

	def getPubKey(self):
		return self.crypto.getPubKey().decode("utf-8")


	# todo: def makeBulkTransactions():

	# opens up /blockchain
	# checks integrity of chain
	# sets self.block
	def syncChain(self):
		try:
			blocks = os.listdir('blockchain/')
		except OSError as err:
			print("key import error\n{0}".format(err))









