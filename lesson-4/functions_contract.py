import os
import json
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

with open("fundme_abi.json") as abi_file:
    abi = json.load(abi_file)
contract_address = Web3.to_checksum_address(
    "0x20651C04f845C6673cE2e9756E27043d78cD1AE8"
)
contract = w3.eth.contract(address=contract_address, abi=abi)

# Send less than minimum required amount to the contract - failed tx
tx_data = {
    "from": account.address,
    "to": contract_address,
    "value": 1,
    "chainId": 11155111,  # Sepolia
    "nonce": w3.eth.get_transaction_count(account.address),
    "gas": 3000000,
    "maxFeePerGas": w3.to_wei("2", "gwei"),
    "maxPriorityFeePerGas": w3.to_wei("1", "gwei"),
}
signed_tx = w3.eth.account.sign_transaction(
    tx_data,
    private_key=private_key,
)
sent_tx = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
print(f"Tx ID: {sent_tx.hex()}")
tx_receipt = w3.eth.wait_for_transaction_receipt(sent_tx)
assert not tx_receipt["status"], "Transactino hasn't failed"

# Send at least 5 usd to the contract - successful tx
amount_to_send = w3.to_wei("0.1", "ether")
assert (
    w3.eth.get_balance(account.address) > amount_to_send
), "Account hasn't enough balance"
tx_data = {
    "from": account.address,
    "to": contract_address,
    "value": amount_to_send,
    "chainId": 11155111,  # Sepolia
    "nonce": w3.eth.get_transaction_count(account.address),
    "gas": 3000000,
    "maxFeePerGas": w3.to_wei("2", "gwei"),
    "maxPriorityFeePerGas": w3.to_wei("1", "gwei"),
}
signed_tx = w3.eth.account.sign_transaction(
    tx_data,
    private_key=private_key,
)
sent_tx = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
print(f"Tx ID: {sent_tx.hex()}")
tx_receipt = w3.eth.wait_for_transaction_receipt(sent_tx)
assert tx_receipt["status"], "Transaction has failed"
assert (
    w3.eth.get_balance(contract.address) == amount_to_send
), "Contract hasn't expected balance"

# Withdrawal funds from contract
tx_data = {
    "chainId": 11155111,  # Sepolia
    "nonce": w3.eth.get_transaction_count(account.address),
    "gas": 3000000,
    "maxFeePerGas": w3.to_wei("2", "gwei"),
    "maxPriorityFeePerGas": w3.to_wei("1", "gwei"),
}
withdrawal_tx = contract.functions.withdrawal().build_transaction(tx_data)
signed_tx = w3.eth.account.sign_transaction(
    withdrawal_tx,
    private_key=private_key,
)
sent_tx = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
print(f"Tx ID: {sent_tx.hex()}")
tx_receipt = w3.eth.wait_for_transaction_receipt(sent_tx)
assert tx_receipt["status"], "Transaction has failed"
assert w3.eth.get_balance(contract.address) == 0, "Contract hasn't expected balance"
