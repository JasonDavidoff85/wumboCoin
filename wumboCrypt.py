from hashlib import sha256
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256
from Crypto.Signature import pkcs1_15

class Crypto:
    def __init__(self):
        self.key = None
        self.hasKey = False

    def createKeyPair(self, keyname = 'wumboKey'):
        self.key = RSA.generate(2048)
        try:
            with open(keyname+'.pem', 'wb') as f:
                f.write(self.key.export_key('PEM'))
            self.hasKey = True
        except:
            print("Uh oh")
            self.key = None
        
    def importKey(self, keyname = 'wumboKey.pem'):
        try:
            with open(keyname, 'r') as f:
                self.key = RSA.import_key(f.read())
            self.hasKey = True
        except OSError as err:
            print("key import error\n{0}".format(err))
            self.hasKey = False
        return self.hasKey

    def hash(self, data):
        data = str(data)
        hashObj = SHA256.new(data=bytes(data, 'utf-8'))
        return hashObj.hexdigest()

    # takes string of data to be signed
    # returns signed byte array
    def sign(self, data):
        if self.hasKey == False:
            print(self.key, "no key")
            return
        hashObj = SHA256.new(data=bytes(data, 'utf-8'))
        signature = pkcs1_15.new(self.key).sign(hashObj)
        return signature

    def verify(self, data, signature):
        if self.hasKey == False:
            print(self.key, "no key")
            return
        hashObj = SHA256.new(data=bytes(data, 'utf-8'))
        try:
            pkcs1_15.new(self.key).verify(hashObj, signature)
            print("Valid Signature!")
            return True
        except (ValueError, TypeError):
            print("The signature is not valid")
            return False

    def getPubKey(self):
        return self.key.publickey().exportKey();

        
        