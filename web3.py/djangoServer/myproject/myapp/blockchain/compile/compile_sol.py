from solcx import install_solc, compile_standard
import json

install_solc("0.8.0")


def compile_contract():
    solidity_file = "tournament.sol"
    contract = "TournamentStorage"
    with open("./" + solidity_file, "r") as f:
        contract_source_code = f.read()

    compiled_sol = compile_standard(
        {
            "language": "Solidity",
            "sources": {solidity_file: {"content": contract_source_code}},
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

    bytecode = compiled_sol["contracts"][solidity_file][contract]["evm"]["bytecode"][
        "object"
    ]
    abi = compiled_sol["contracts"][solidity_file][contract]["abi"]

    with open("bytecode.txt", "w") as bytecode_file:
        bytecode_file.write(bytecode)

    with open("abi.json", "w") as abi_file:
        json.dump(abi, abi_file)


compile_contract()
