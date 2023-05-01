from web3 import Web3

from creds import INFURA_API_KEY


web3 = Web3(Web3.HTTPProvider(INFURA_API_KEY))
print(f'Connected: {web3.is_connected()}')
