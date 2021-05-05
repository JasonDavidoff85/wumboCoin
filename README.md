# WumboCoin

## How it works
WumboCoin is a decentralized blockchain cryptocurrency using sha256
The block structure is basically just bitcoin's but slightly more simplified

### Differences
* WumboCoin assigns a block reward of a random value of WumboCoin (1-6)

## How it runs

*TODO figure out how to start process*

## API

WumboCoin runs as a api using a flask server

### API Reference


* `POST /api/authenticate/`
**Logs user in**
Takes json object with format
`{'username': {username}, 'password': {receiver}}`

* `POST /api/user/`
**create user**
Takes json obj in format:
`{'username': {username}, 'password': {password}}`

#### The following api calls *require authentication*

* `POST /api/addTransaction/`
**Add transaction to current block**
Takes json object in format:
`{'receiver': {receiver}, 'amount': {amount}}`

* `POST /api/importKey/`
**sends key to api server**
Takes json obj in format:
`{'pub': {pubKey}, 'pri': {priKey}}`

* `GET /api/makeKeys/`
**Returns json with pub and pri key**
Returns obj in format:
`{'pub': {pubKey}, 'pri': {priKey}}`

* `GET /api/block/{block number}`
**Returns json of block**

* `GET /api/user/{username}`
**Returns json of public facing info on the user**





