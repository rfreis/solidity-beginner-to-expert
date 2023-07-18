import os
import json
from compile_contract import compiled_fundme
from eth_account import Account
from eth_account.signers.local import LocalAccount
from web3 import Web3

apikey = os.environ.get("INFURA_APIKEY")
apisecret = os.environ.get("INFURA_APISECRET")
private_key = os.environ.get("PRIVATE_KEY")
account: LocalAccount = Account.from_key(private_key)

url = f"https://:{apisecret}@sepolia.infura.io/v3/{apikey}"


w3 = Web3(Web3.HTTPProvider(url))
assert w3.is_connected(), "Provider not connected!"

chainlink_id = "@chainlink/contracts/src/v0.8/interfaces/AggregatorV3Interface.sol:AggregatorV3Interface"
fundme_id = "FundMe.sol:FundMe"
price_converter_id = "PriceConverter.sol:PriceConverter"

fundme_bytecode = compiled_fundme[fundme_id]["bin"]
fundme_abi = compiled_fundme[fundme_id]["abi"]
FundMe = w3.eth.contract(abi=fundme_abi, bytecode=fundme_bytecode)

tx_data = {
    "chainId": 11155111,  # Sepolia
    "nonce": w3.eth.get_transaction_count(account.address),
    "gas": 3000000,
    "maxFeePerGas": w3.to_wei("2", "gwei"),
    "maxPriorityFeePerGas": w3.to_wei("1", "gwei"),
}
transaction = FundMe.constructor().build_transaction(tx_data)
signed_tx = w3.eth.account.sign_transaction(
    transaction,
    private_key=private_key,
)
sent_tx = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
print(f"Tx ID: {sent_tx.hex()}")
tx_receipt = w3.eth.wait_for_transaction_receipt(sent_tx)
print(f"Contract Address: {tx_receipt['contractAddress']}")


with open("fundme_abi.json", "w") as fundme_abi_json:
    fundme_abi_json.write(json.dumps(fundme_abi, indent=4))
