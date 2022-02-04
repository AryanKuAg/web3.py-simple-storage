# import compile_standard from solcx
from dis import Bytecode
from traceback import print_tb
from solcx import compile_standard, install_solc
from web3 import Web3
import json
import os
from dotenv import dotenv_values, load_dotenv

load_dotenv()

with open("./SimpleStorage.sol",  'r') as f:
    simpleStorage = f.read()
    # print(simpleStorage)

# Compile our solidity
install_solc("0.8.11")
compiled_sol = compile_standard(
    {"language": "Solidity",
     "sources": {"SimpleStorage.sol":  {"content": simpleStorage}},
     "settings": {
         "outputSelection": {
             "*": {"*": ["abi", "metadata", "evm.bytecode", "evm.sourceMap"]}
         }
     }
     },
    solc_version="0.8.11"
)

# print(compiled_sol)

with open("compiled_code.json", 'w') as file:
    json.dump(compiled_sol, file)

# get byte code
with open("compiled_code.json", 'r') as a_file:
    data = json.load(a_file)

byte_code = data["contracts"]["SimpleStorage.sol"]["SimpleStorage"]["evm"]["bytecode"]["object"]

# print(byte_code)
# get abi
abi = data["contracts"]["SimpleStorage.sol"]["SimpleStorage"]["abi"]
# print(abi)

# to connect to ganache
w3 = Web3(Web3.HTTPProvider("HTTP://127.0.0.1:7545"))
chain_id = 1337
my_address = '0x1b3956c81aF861ff5E6982cF76D81AA3FE7aC53d'
private_key = os.getenv("PRIVATE_KEY")

config = dotenv_values(".env")
# print(config.get('PRIVATE_KEY'))

# creating a contract in python
SimpleStorage = w3.eth.contract(abi=abi, bytecode=byte_code)

# get the latest or number of trasnsactions
nonce = w3.eth.getTransactionCount(my_address)
# print(nonce)

transaction = SimpleStorage.constructor().buildTransaction(
    {"gasPrice": w3.eth.gas_price, "chainId": chain_id, "from": my_address, "nonce": nonce})
# print(transaction)

# signing my transaction with private key
signed_txn = w3.eth.account.sign_transaction(
    transaction, private_key=config.get('PRIVATE_KEY'))

# deploy the transaction
tx_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)
