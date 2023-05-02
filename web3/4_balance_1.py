from web3 import Web3

from creds import INFURA_API_KEY, ERC_20_WALLET_ADDRESS


web3 = Web3(Web3.HTTPProvider(INFURA_API_KEY))

erc20_abi = [
    {
        "inputs": [],
        "name": "name",
        "outputs": [
            {
                "internalType": "string",
                "name": "",
                "type": "string"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    }
]

# retrieve balance of all tokens on account
for token_address in web3.eth.accounts:
    try:
        contract = web3.eth.contract(address=token_address, abi=erc20_abi)
        name = contract.functions.name().call()
        balance = contract.functions.balanceOf(ERC_20_WALLET_ADDRESS).call()
        if balance > 0:
            print(f"{name} ({balance})")
    except:
        continue
