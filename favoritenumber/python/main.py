from web3 import Web3
import json, web3

server = "HTTP://127.0.0.1:7545"
id = 5777
private_key = "443fef73e0ae67ee14f49ba7e5430b01646af5c2b5966f49cba8c42f2553275f"
public_add = "0x2DD2D553f41a9Ab95347C2A21d080559443C8FEa"

public_add2 = "0x9C4486F021E2551854f2F720134F91b8d8C53e2c"

def get_abi(name):
    data = json.load(open(name))
    return {"abi": data["abi"], "bytecode": data["bytecode"]}

w3 = Web3(Web3.HTTPProvider(server))
w3.isConnected()
w3.eth.get_block('latest')

address = "0x19817df3224bE622F19D08445ca1Ffc317AeC174"

contract = w3.eth.contract(address=address, **get_abi("favoritenumber/build/contracts/FavoriteNumber.json"))
contract.functions.getFavoriteNumber().call()
# Ceci ne marche pas  -- contract.functions.setFavoriteNumber(42).call()
contract.functions.getFavoriteNumber().call()


txn = contract.functions.setFavoriteNumber(
    20,
).build_transaction({
    'nonce': w3.eth.get_transaction_count(public_add),
    'gas': 2000000,
    'gasPrice': w3.toWei('50', 'gwei')
})
signed_txn = w3.eth.account.sign_transaction(txn, private_key=private_key)
w3.eth.send_raw_transaction(signed_txn.rawTransaction) 

# Transfert d'argent

#get the nonce.  Prevents one from sending the transaction twice
nonce = w3.eth.get_transaction_count(public_add)

#build a transaction in a dictionary
tx = {
    'nonce': nonce,
    'to': public_add2,
    'value': w3.toWei(1, 'ether'),
    'gas': 2000000,
    'gasPrice': w3.toWei('50', 'gwei')
}

#sign the transaction
signed_tx = w3.eth.account.sign_transaction(tx, private_key)

#send transaction
tx_hash = w3.eth.sendRawTransaction(signed_tx.rawTransaction)
