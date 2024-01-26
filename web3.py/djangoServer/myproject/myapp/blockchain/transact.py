from web3 import Web3
from dotenv import load_dotenv
import os
import json
import os


def get_bytecode_and_abi():
    bytecode_file_path = ""
    abi_file_path = ""

    for root, dirs, files in os.walk(".", topdown=True):
        for file in files:
            if file == "bytecode.txt":
                bytecode_file_path = os.path.join(root, file)
            elif file == "abi.json":
                abi_file_path = os.path.join(root, file)

    with open(bytecode_file_path, "r") as bytecode_file:
        bytecode = bytecode_file.read()

    with open(abi_file_path, "r") as abi_file:
        abi = json.load(abi_file)

    return bytecode, abi


def deploy_contract(bytecode, abi):
    SimpleStorage = w3.eth.contract(abi=abi, bytecode=bytecode)
    nonce = w3.eth.get_transaction_count(my_address)
    transaction = SimpleStorage.constructor().build_transaction(
        {"chainId": chain_id, "from": my_address, "nonce": nonce}
    )
    signed_txn = w3.eth.account.sign_transaction(transaction, private_key=private_key)
    print("Making New Contract!")
    tx_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)
    tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
    print("Deployed!")

    return tx_receipt


def retrieve_transaction(tx_receipt, abi):
    simple_storage = w3.eth.contract(address=tx_receipt.contractAddress, abi=abi)
    print("retrive transcation! !!:", simple_storage.functions.retrieve().call())
    tournaments = simple_storage.functions.retrieve().call()
    tournament_log = []
    for tournament in tournaments:
        tournament_dict = []
        for game in tournament:
            game_id, winner, loser = game
            game_dict = {
                "game_id": game_id,
                "winner": {"name": winner[0], "score": winner[1]},
                "loser": {"name": loser[0], "score": loser[1]},
            }
            tournament_dict.append(game_dict)
        tournament_log.append({"tournament": tournament_dict})

    tournament_log_data = {"tournamentLog": tournament_log}

    # 딕셔너리를 JSON 형태로 변환
    json_data = json.dumps(tournament_log_data, ensure_ascii=False, indent=4)

    return json_data
    print(json_data)
    json_tournaments = json.dumps(tournaments)
    print("json_tournament!!! :", json_tournaments)
    return json_tournaments


def record_transaction(tx_receipt, abi, tournament):
    simple_storage = w3.eth.contract(address=tx_receipt.contractAddress, abi=abi)
    nonce = w3.eth.get_transaction_count(my_address)

    add_transaction = simple_storage.functions.store(tournament).build_transaction(
        {"chainId": chain_id, "from": my_address, "nonce": nonce}
    )
    signed_add_txn = w3.eth.account.sign_transaction(
        add_transaction, private_key=private_key
    )
    send_add_tx = w3.eth.send_raw_transaction(signed_add_txn.rawTransaction)
    tx_receipt = w3.eth.wait_for_transaction_receipt(send_add_tx)

    print("add_transaction!!! :", tournament)


load_dotenv()
w3 = Web3(Web3.HTTPProvider(os.environ.get("WEB3_PROVIDER")))
chain_id = int(os.environ.get("CHAIN_ID"))
my_address = os.environ.get("MY_ADDRESS")
private_key = os.getenv("PRIVATE_OWNER_KEY")


bytecode, abi = get_bytecode_and_abi()
tx_receipt = deploy_contract(bytecode, abi)


def makePlayer(name, score):
    return {"name": name, "score": score}


def addGameLog(winner, loser, order, tournament):
    tournament.append({"game_id": order, "winner": winner, "loser": loser})


tournament = []
addGameLog(makePlayer("a", 1), makePlayer("b", 2), 1, tournament)
addGameLog(makePlayer("c", 3), makePlayer("d", 4), 2, tournament)
addGameLog(makePlayer("e", 5), makePlayer("f", 6), 3, tournament)

record_transaction(tx_receipt, abi, tournament)

tournament = []
addGameLog(makePlayer("e", 1), makePlayer("f", 2), 1, tournament)
addGameLog(makePlayer("c", 3), makePlayer("d", 4), 2, tournament)
addGameLog(makePlayer("a", 5), makePlayer("b", 6), 3, tournament)


record_transaction(tx_receipt, abi, tournament)

retrieve_transaction(tx_receipt, abi)
