from web3 import Web3
import json, web3

server = "HTTP://127.0.0.1:7545"
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
address = "0x3447219E201420A088Eb538C5e39317388985CB4"

contract = w3.eth.contract(address=address, **get_abi("getReserve/build/contracts/UniswapTrue.json"))

contract.all_functions()

contract.functions.getReserves().call()
