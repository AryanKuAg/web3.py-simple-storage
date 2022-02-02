# import compile_standard from solcx
from solcx import compile_standard

with open("./SimpleStorage.sol",  'r') as f:
    simpleStorage = f.read()
    print(simpleStorage)

# Compile our solidity

compiled_sol = compile_standard(
    {"language": "Solidity",
     "sources": {"SimpleStorage.sol":  {"content": simpleStorage}},
     "settings": {
         "outputSelection": {
             "*": {"*": ["abi", "metadata", "evm.bytecode", "evm.sourceMap"]}
         }
     }
     },
    solc_version="0.6.0"
)

print(compiled_sol)
