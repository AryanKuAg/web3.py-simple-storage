# import compile_standard from solcx
from solcx import compile_standard, install_solc

with open("./SimpleStorage.sol",  'r') as f:
    simpleStorage = f.read()
    print(simpleStorage)

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

print(compiled_sol)
