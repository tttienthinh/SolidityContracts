from web3 import Web3
import json, web3

server = "HTTP://127.0.0.1:7545"
server = "https://eth-goerli.public.blastapi.io"
"""
Goerli : 
a.sol : 0x4e2341943F7684ef8C9F30A1a516f47797Dd5e3c
aGet.sol : 0xa619FD5Ca1F24e8e94cB51D874d7cbDD5e07937D

change name AName : 
a.sol : 0x8CAbFb3191698c7a96364a03838A785a52dDc347
aGet.sol : 0xcEF60c245acb53614CB4B9D38c5e2c430c6c402B

change name a_get : 
aGet.sol : 0xC29A43Bb343859F0C0309A2c009A25F230B13E70
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
address = "0xC29A43Bb343859F0C0309A2c009A25F230B13E70"

contract = w3.eth.contract(address=address, **get_abi("evolution/build/contracts/a_get.json"))

contract.all_functions()

contract.functions.getA("0x4e2341943F7684ef8C9F30A1a516f47797Dd5e3c").call()
contract.functions.getA2("0x4e2341943F7684ef8C9F30A1a516f47797Dd5e3c").call()
