from wumboCoin import wumboCoin

wumbo = wumboCoin('Jason', 'pass', 'ledger.json')

wumbo.makeKeys()

wumbo.giveCoins('Test', 4)