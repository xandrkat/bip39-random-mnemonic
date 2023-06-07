from mnemonic import Mnemonic
import bip32utils
import random
import requests

mnemon = Mnemonic('english')
#words = mnemon.generate(256)
#print(words)
#mnemon.check(words)
#seed = mnemon.to_seed(words)
nums = {}
wordlist = []
mnemo = ''
with open('english.txt') as fin:
    i = 0
    for word in fin:
        nums[word.strip()] = i
        wordlist.append(word.strip())
        i += 1
i = 0
for x in range(0, 2048):
  i=i+1
  mnemo =  'abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon ' + wordlist[i]
  seed = mnemon.to_seed(mnemo)
  root_key = bip32utils.BIP32Key.fromEntropy(seed)
  address = root_key.Address()
  balance = requests.get("https://blockchain.info/balance?active=" + str(address))
  print(str(mnemo))
  print(str(address) + ': ' + str(balance.json()[str(address)]['final_balance']))
  mnemo = ''

#root_key = bip32utils.BIP32Key.fromEntropy(seed)
#root_address = root_key.Address()
#root_public_hex = root_key.PublicKey().hex()
#root_private_wif = root_key.WalletImportFormat()
#print('Root key:')
#print(f'\tAddress: {root_address}')
#print(f'\tPublic : {root_public_hex}')
#print(f'\tPrivate: {root_private_wif}\n')

#child_key = root_key.ChildKey(0).ChildKey(0)
#child_address = child_key.Address()
#child_public_hex = child_key.PublicKey().hex()
#child_private_wif = child_key.WalletImportFormat()
#print('Child key m/0/0:')
#print(f'\tAddress: {child_address}')
#print(f'\tPublic : {child_public_hex}')
#print(f'\tPrivate: {child_private_wif}\n')
