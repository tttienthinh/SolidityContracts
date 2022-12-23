from web3 import Web3
import json, web3

server = "https://eth-goerli.public.blastapi.io"
id = 5777
private_key = "df49b58fbc863c5e60fe4e64829a853c46a8a12c3310404bc2a03bfefb89f68a"
public_add = "0xb4311ad11530F735ecE2d652Cbd56D1FB8D6Efeb"

public_add2 = "0x9C4486F021E2551854f2F720134F91b8d8C53e2c"

def get_abi(name):
    data = json.load(open(name))
    return {"abi": data["abi"], "bytecode": data["bytecode"]}

w3 = Web3(Web3.HTTPProvider(server))
w3.isConnected()

# Contrat intermédiaire
address = "0x97BdDaff1a971580f99C1DB850dE5EcF4982251a"

contract = w3.eth.contract(address=address, **get_abi("tests/build/contracts/ExistingNoSet.json"))

contract.all_functions()

contract.functions.getA("0x14c89b4F462C11961Bb48aD6B2008f64617CF62a").call()


txn = contract.functions.setA(
    "0x14c89b4F462C11961Bb48aD6B2008f64617CF62a", 15
).build_transaction({
    'nonce': w3.eth.get_transaction_count(public_add),
    'gas': 200000,
    'gasPrice': w3.toWei('20', 'gwei')
})
signed_txn = w3.eth.account.sign_transaction(txn, private_key=private_key)
w3.eth.send_raw_transaction(signed_txn.rawTransaction) 
