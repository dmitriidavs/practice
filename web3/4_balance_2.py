import json

from moralis import evm_api

from creds import MORALIS_API_KEY, ERC_20_WALLET_ADDRESS


acc_balance = evm_api.token.get_wallet_token_balances(
    api_key=MORALIS_API_KEY,
    params={
        'address': ERC_20_WALLET_ADDRESS,
        'chain': 'eth',
    }
)

for token in acc_balance:
    print(f'{token["name"]}({token["symbol"]}): {int(token["balance"]) / 10 ** token["decimals"]}')
