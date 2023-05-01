from web3 import Web3

from creds import INFURA_API_KEY, ERC_20_TARGET_ADDRESS, ERC_20_WALLET_ADDRESS


def address_is_wallet(account: Web3.to_checksum_address) -> bool:
    account_bytecode = web3.eth.get_code(account)
    if account_bytecode == b'':
        return True
    else:
        return False


def address_is_contract(account: Web3.to_checksum_address) -> tuple[bool, str]:
    account_bytecode = web3.eth.get_code(account)
    if account_bytecode != b'':
        return True, web3.to_hex(account_bytecode)
    else:
        return False, ''


if __name__ == '__main__':
    web3 = Web3(Web3.HTTPProvider(INFURA_API_KEY))
    target_address = web3.to_checksum_address(ERC_20_TARGET_ADDRESS)
    # target_address = web3.to_checksum_address(ERC_20_WALLET_ADDRESS)

    if address_is_wallet(target_address):
        print(f'Address: {target_address}\n'
              f'Balance: {web3.from_wei(web3.eth.get_balance(target_address), "ether")} ETH')

    address_is_contract = address_is_contract(target_address)
    if address_is_contract[0]:
        print(f'Address: {target_address}\n'
              f'Bytecode: {address_is_contract[1]}')
