from web3 import Web3

INFURA_API_KEY = ''

web3 = Web3(Web3.HTTPProvider(INFURA_API_KEY))
print(f'Connected: {web3.is_connected()}')

target_address = web3.toCkecksumAddress('')
target_ABI = ''
terget = web3.eth.contract(address=target_address, abi=target_ABI)
