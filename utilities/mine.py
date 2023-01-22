import hashlib
import requests
import json
import sys

LEADINGZERO = 25
lower = 0
higher = 0

if len(sys.argv) < 2:
    print("requires argument of number to test up to")
    exit(1)

if len(sys.argv) >= 3:
    lower = int(sys.argv[1])
    higher = int(sys.argv[2])
else:
    higher = int(sys.argv[1])

resp = requests.get('http://127.0.0.1:3000/api/getBlock/1').json()
print(resp)
proofOfWork = 0
blockHash = ''
for i in range(lower, higher):
    resp["header"]["proofOfWork"] = i
    m = hashlib.sha256()
    m.update(json.dumps(resp).encode('utf-8'))
    output = ''.join(map(lambda x: '{:08b}'.format(x), m.digest()))
    print("\n" + output)
    if output[:LEADINGZERO] == '0' * LEADINGZERO:
        proofOfWork = i
        blockHash = m.hexdigest()
        break
    

if proofOfWork != 0:
    print(f"============\nBlock Mined!\nProof of work: {proofOfWork}")
    print(f"Block Hash: {blockHash}")
else:
    print(f"Could not mine block in range {lower}-{higher}")