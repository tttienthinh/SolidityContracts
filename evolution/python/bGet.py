from web3 import Web3
import json, web3

server = "HTTP://127.0.0.1:7545"
server = "https://eth-goerli.public.blastapi.io"
"""
Goerli : 
b.sol : 0x23a2F666Bb3868121661b6Cfe5839035fC0772C2
bGet.sol : 0x064BE8Bed899B1Ed06b653178eB129d00f919CAc

changing name to b and b_get :
b.sol : 0x04E7F159B0bA7C97BBe695bF6813Ee2AC5911518
bGet.sol : 0x27259465fBD020f7DCeBFBE42B95691CD1FA7dCE (not working)

changing name Favorite:
bGet.sol : 0x9d2470539c874F27db606527C9f441109f1d346b

changing name favorite:
bGet.sol : 0x1eC7D24b607F8b01367903bDD677b2b8B0bc1863

changing name b_get:
bGet.sol : 0xe86719aa97b550EA4c071c48EfE0eb9f78c8002B

changing name b:
bGet.sol : 0x7b44988f84C93A34542a88e942cEC18bc544ad3c

changing name c:
bGet.sol : 0x1d3000322bE3B838e9bd8FcCed6B14662c9f25A8
"""
private_key = "df49b58fbc863c5e60fe4e64829a853c46a8a12c3310404bc2a03bfefb89f68a"
public_add = "0xb4311ad11530F735ecE2d652Cbd56D1FB8D6Efeb"

public_add2 = "0x9C4486F021E2551854f2F720134F91b8d8C53e2c"

def get_abi(name):
    data = json.load(open(name))
    return {"abi": data["abi"], "bytecode": data["bytecode"]}

w3 = Web3(Web3.HTTPProvider(server))
w3.isConnected()

# Contrat intermédiaire
address = "0x1d3000322bE3B838e9bd8FcCed6B14662c9f25A8"

contract = w3.eth.contract(address=address, **get_abi("evolution/build/contracts/b_get.json"))

contract.all_functions()

contract.functions.getA("0x04E7F159B0bA7C97BBe695bF6813Ee2AC5911518").call()

txn = contract.functions.setA(
    "0x04E7F159B0bA7C97BBe695bF6813Ee2AC5911518", 15
).build_transaction({
    'nonce': w3.eth.get_transaction_count(public_add),
    'gas': 2000000,
    'gasPrice': w3.toWei('50', 'gwei')
})
signed_txn = w3.eth.account.sign_transaction(txn, private_key=private_key)
w3.eth.send_raw_transaction(signed_txn.rawTransaction) 

contract.functions.getA("0x23a2F666Bb3868121661b6Cfe5839035fC0772C2").call()


