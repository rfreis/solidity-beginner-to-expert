import os
import json
from web3 import Web3

apikey = os.environ.get("INFURA_APIKEY")
apisecret = os.environ.get("INFURA_APISECRET")
private_key = os.environ.get("PRIVATE_KEY")

url = f"https://:{apisecret}@sepolia.infura.io/v3/{apikey}"


w3 = Web3(Web3.HTTPProvider(url))
assert w3.is_connected(), "Provider not connected!"

contract_address = Web3.to_checksum_address("0x62c338bd5ac1cedfc6e7b5a2287443f0e1817931")
with open("abi.json") as abi_file:
    abi = json.load(abi_file)
contract = w3.eth.contract(address=contract_address, abi=abi)

# Sent using remix and Metamask
first_person = contract.functions.listOfPeople(0).call()
print(f"First Person, defined using Remix and Metamask: {first_person}")

# Create second person using this snippet
add_second_person_tx = contract.functions.addPerson("Using Python", 200).build_transaction({
    "chainId": 11155111, # Sepolia
    "gas": 3000000,
    "maxFeePerGas": w3.to_wei("2", "gwei"),
    "maxPriorityFeePerGas": w3.to_wei("1", "gwei"),
    "nonce": 2,
})
signed_tx = w3.eth.account.sign_transaction(
    add_second_person_tx,
    private_key=private_key,
)
sent_tx = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
print(f"Tx ID: {sent_tx.hex()}")

# Sent using the snippet above
second_person = contract.functions.listOfPeople(1).call()
print(f"Second Person, defined using this snippet: {second_person}")

# Get second person number using the mapping storage
second_person_number = contract.functions.nameToFavoriteNumber("Using Python").call()
print(f"Second Person Number, from mapping: {second_person_number}")
