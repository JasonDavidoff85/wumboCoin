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

class wumboCoin():
	def __init__(self):
		self.crypto = Crypto()
		# set current block
		self.block = Block('blockchain/current.wub')

	def authenticate(self, username, password):
		#use db interface to check username and password
		return
		
	def importKey(self, path):
		self.crypto.importKey(path)
	
	def makeKeys(self, keyname):
		self.crypto.createKeyPair(keyname)

	# opens each block and sums up user 
	def getBalance(self, username):
		return 0
	def __getCurrentHeight(self):
		return 0


	def giveCoins(self, receiver, amount):
		#__checkIfPossible()
		transaction = {'sender': self.username, 'receiver': receiver, 'amount': amount}
		self.block.addTransaction(transaction, self.key.publickey().exportKey())

	# todo: def makeBulkTransactions():

	def writeToLedger(self):
		existing = {}
		with open('ledger.json', 'r') as f:
			exisiting = json.load(f)
		exisiting.update(self.currBlock.export())
		with open('ledger.json', 'w') as f:
			json.dump(exisiting, f)

	# opens up /blockchain
	# checks integrity of chain
	# sets self.block
	def syncChain(self):
		try:
			blocks = os.listdir('blockchain/')
		except OSError as err:
			print("key import error\n{0}".format(err))









