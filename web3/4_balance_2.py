import json

from moralis import evm_api

from creds import MORALIS_API_KEY, ERC_20_WALLET_ADDRESS


params = {
    'address': ERC_20_WALLET_ADDRESS,
    'chain': 'eth',
}

acc_balance = evm_api.token.get_wallet_token_balances(
    api_key=MORALIS_API_KEY,
    params=params
)

for token in acc_balance:
    print(f'{token["name"]}({token["symbol"]}): {int(token["balance"]) / 10 ** token["decimals"]}')

print('*' * 150)

acc_transactions = evm_api.token.get_wallet_token_transfers(
    api_key=MORALIS_API_KEY,
    params=params
)


def get_symbol(address: str) -> dict:
    return evm_api.token.get_token_metadata(
        api_key=MORALIS_API_KEY,
        params={
            'addresses': (address,),
            'chain': 'eth'
        }
    )[0]["name"]


# print(json.dumps(acc_transactions, indent=4))

for tran in acc_transactions["result"]:
    if tran["possible_spam"] is False:
        print(f'[{tran["block_timestamp"]}] {get_symbol(tran["address"])}: {int(tran["value"]) / 10 ** 18}\n'
              f'To: {tran["to_address"]}')
