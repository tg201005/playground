##pip install web3
from web3 import Web3
from solcx import install_solc

install_solc("0.8.0")

from solcx import compile_standard
import json

with open("./simpleStorage.sol", "r") as f:
    contract_source_code = f.read()

## pip install solc
## pip install py-solc-x

compiled_sol = compile_standard(
    {
        "language": "Solidity",
        "sources": {"simpleStorage.sol": {"content": contract_source_code}},
        "settings": {
            "outputSelection": {
                "*": {"*": ["abi", "metadata", "evm.bytecode", "evm.sourceMap"]}
            }
        },
    },
    solc_version="0.8.0",
)

with open("compiled_code.json", "w") as file:
    json.dump(compiled_sol, file)

# get bytecode
bytecode = compiled_sol["contracts"]["simpleStorage.sol"]["SimpleStorage"]["evm"][
    "bytecode"
]["object"]
abi = compiled_sol["contracts"]["simpleStorage.sol"]["SimpleStorage"]["abi"]


# for connecting to ganache

from dotenv import load_dotenv
import os

load_dotenv()

w3 = Web3(Web3.HTTPProvider(os.environ.get("WEB3_PROVIDER")))
chain_id = int(os.environ.get("CHAIN_ID"))
my_address = os.environ.get("MY_ADDRESS")
private_key = os.getenv("PRIVATE_OWNER_KEY")


# create the contract in python
SimpleStorage = w3.eth.contract(abi=abi, bytecode=bytecode)


nonce = w3.eth.get_transaction_count(my_address)
# 1. build a transaction

transaction = SimpleStorage.constructor().build_transaction(
    {"chainId": chain_id, "from": my_address, "nonce": nonce}
)


# 2. sign a transaction

sighned_txn = w3.eth.account.sign_transaction(transaction, private_key=private_key)

# 3. send a transaction

print("Deploying Contract!")
tx_hash = w3.eth.send_raw_transaction(sighned_txn.rawTransaction)
tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)

print("Deployed!")
### working with deployed contracts
## contract address
## contract ABI
simple_storage = w3.eth.contract(address=tx_receipt.contractAddress, abi=abi)

# call  -> simultae to read in blue remix
# transact -> actually make a state change in orange button remix


##initial value of favorite number
print(simple_storage.functions.retrieve().call())


print("Updating Contract!")
store_transaction = simple_storage.functions.store(15).build_transaction(
    {"chainId": chain_id, "from": my_address, "nonce": nonce + 1}
)
signed_store_txn = w3.eth.account.sign_transaction(
    store_transaction, private_key=private_key
)
send_store_tx = w3.eth.send_raw_transaction(signed_store_txn.rawTransaction)
tx_receipt = w3.eth.wait_for_transaction_receipt(send_store_tx)
print("Updated!")
print(simple_storage.functions.retrieve().call())
