from web3 import Web3

from creds import INFURA_API_KEY, ERC_20_TARGET_ADDRESS, ERC_20_TARGET_ABI


web3 = Web3(Web3.HTTPProvider(INFURA_API_KEY))
print(f'Connected: {web3.is_connected()}')

target_address = web3.to_checksum_address(ERC_20_TARGET_ADDRESS)
target_ABI = ERC_20_TARGET_ABI
target = web3.eth.contract(address=target_address, abi=target_ABI)

print(f'name: {target.functions.name().call()}')
print(f'symbol: {target.functions.symbol().call()}')
print(f'totalSupply_1: {target.functions.totalSupply().call() / 10 ** target.functions.decimals().call()}')
print(f'totalSupply_2: {web3.from_wei(target.functions.totalSupply().call(), "ether")}')
print(f'minimumTimeBetweenMints: {target.functions.minimumTimeBetweenMints().call()}')
