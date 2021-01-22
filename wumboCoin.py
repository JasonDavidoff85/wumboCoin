import json
import gnupg
from hashlib import sha256
from Crypto.PublicKey import RSA

# transaction:
# 	id:
# 	sender:
# 	receiver:
# 	amount:
# sender key
# transaction signature



class wumboCoin():
	def __init__(self, username, password, ledger):
		self.username = username
		self.password = password
		self.ledger = ledger
		self.has_key = False


	# def __init__(self, username, password, ledger, keyPair):
	# 	self.username = username
	# 	self.password = password
	# 	self.ledger = ledger
	# 	try:
	# 		self.pubKey = {"n": keyPair.n, "e": keyPair.e}
	# 		self.privKey = {"n": keyPair.n, "d": keyPair.d}
	# 	except:
	# 		print("Ket not valid")
	# 		exit(0)
	# 	self.has_key = True

	def makeKeys(self):
		keyPair = RSA.generate(bits=1024)
		self.pubKey = {"n": keyPair.n, "e": keyPair.e}
		self.privKey = {"n": keyPair.n, "d": keyPair.d}

	def __checkIfPossible(self):
		return 0
	def __getCurrentHeight(self):
		return 0


	def giveCoins(self, receiver, amount):
		#__checkIfPossible()
		#height = __getCurrentHeight()
		transaction = {height: {'sender': self.username, 'receiver': receiver, 'amount': amount}}
		m = sha256((str(height)+str(transaction[height])).encode('utf-8'))
		hashed = int.from_bytes(m.digest(), byteorder='big')
		signature = pow(hashed, self.privKey['d'], self.privKey['n'])
		ledger = {}
		ledger[i] = {
			'transaction': transaction[height],
			'hash': hex(hashed),
			'signature': hex(signature),
			'key': {'n': hex(self.pubKey['n']), 'e': hex(self.pubKey['e'])}
		}
		data = {}
		with open(self.ledger, "r") as file:
			data = json.load(file)
			data.update(ledger)

		with open(self.ledger, "w") as file:
			json.dump(data, file)

	# todo: def makeBulkTransactions():


	def inital_transactions(self):
		transactions = {
			0: {'sender': 'wumbo', 'receiver': 'Jason', 'amount': 17},
			1: {'sender': 'Jason', 'receiver': 'Hannah & Joey', 'amount': 6},
			2: {'sender': 'Jason', 'receiver': 'Phaedra', 'amount': 5},
			3: {'sender': 'Jason', 'receiver': 'John and Paola', 'amount': 4},
			4: {'sender': 'Jason', 'receiver': 'Nick', 'amount': 2}
		}
		ledger = {}

		for i, k in transactions.items():
			m = sha256((str(i)+str(k)).encode('utf-8'))
			hashed = int.from_bytes(m.digest(), byteorder='big')
			signature = pow(hashed, privKey['d'], privKey['n'])
			ledger[i] = {
				'transaction': k,
				'hash': hex(hashed),
				'signature': hex(signature),
				'key': {'n': hex(pubKey['n']), 'e': hex(pubKey['e'])}
			}

		print(ledger)

		print(int(ledger[2]['hash'], 16) == pow(int(ledger[2]['signature'], 16), pubKey['e'], pubKey['n']))
		
		with open("ledger.json", "w") as file:
			json.dump(ledger, file)







