# import compile_standard from solcx
from solcx import compile_standard, install_solc
from web3 import Web3
import json
import os
from dotenv import dotenv_values

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

byte_code = data["contracts"]["SimpleStorage.sol"]["SimpleStorage"]["evm"]["bytecode"]["opcodes"]

print(byte_code)

# # to connect to ganache
# w3 = Web3(Web3.HTTPProvider("HTTP: // 127.0.0.1:7545"))
# private_key = os.getenv("PRIVATE_KEY")

# config = dotenv_values(".env")
# print(config)
