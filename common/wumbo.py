import json
import os
from .wumboCrypt import Crypto
from common.block import Block
from models import Blockchain
from db import db
#import gnupg

# transaction:
# 	id:
# 	sender:
# 	receiver:
# 	amount:
# sender key
# transaction signature

# create a wumbo to interact with the blockchain
class wumbo():
	def __init__(self, privKey=None):
		self.crypto = Crypto(privKey)
		# set current block
		# TODO BUG have some sort of alias or protocol for current 
		# incase one isnt named that
		self.block = self.getMostRecentBlock()

	def getMostRecentBlock(self):
		return Block(self, file=Blockchain.query.filter_by(current=True).first().wub_file)
		
	def importKey(self, path):
		self.crypto.importKey(path)
	
	def makeKeys(self):
		return self.crypto.createKey()

	def giveCoins(self, sender, receiver, amount):
		transaction = {"sender": sender, "receiver": receiver, "amount": amount}
		return self.block.addTransaction(transaction)

	def getBlock(self, blockNum):
		return Block(None, file=Blockchain.query.get(int(blockNum)).wub_file)

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









