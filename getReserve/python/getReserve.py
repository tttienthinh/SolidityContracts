from web3 import Web3
import json, web3

server = "HTTP://127.0.0.1:7545"
server = "https://eth-goerli.public.blastapi.io"
"""
Goerli : 
IUniswapV2Pair.sol : 0x1b7F3508B786DC531EC7A77EAb7FF08127437837  
getReserve.sol : 0x3b0C3dECE70Eb7E289bec7D51D7eFBfCd7e1E43c
"""

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
address = "0x3b0C3dECE70Eb7E289bec7D51D7eFBfCd7e1E43c"

contract = w3.eth.contract(address=address, **get_abi("getReserve/build/contracts/middleMan.json"))

contract.all_functions()

contract.functions.getList(["0x1b7F3508B786DC531EC7A77EAb7FF08127437837", "0x33e57A530F90aB2A5572E2a877161Ca644e8FC95", "0xc76531Bb08e8E266E4eB8a988D314AA6650292af"]).call()


contract.functions.getOnlyOne("0x1b7F3508B786DC531EC7A77EAb7FF08127437837").call()


