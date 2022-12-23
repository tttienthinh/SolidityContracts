from web3 import Web3
import json, web3

server = "https://eth-goerli.public.blastapi.io"
id = 5777
private_key = "df49b58fbc863c5e60fe4e64829a853c46a8a12c3310404bc2a03bfefb89f68a"
public_add = "0xb4311ad11530F735ecE2d652Cbd56D1FB8D6Efeb"

public_add2 = "0x9C4486F021E2551854f2F720134F91b8d8C53e2c"


w3 = Web3(Web3.HTTPProvider(server))
w3.isConnected()

abi = [
		{
			"inputs": [
                {
                "internalType": "address",
                "name": "factory",
                "type": "address"
                },
                {
                "internalType": "address",
                "name": "tokenA",
                "type": "address"
                },
                {
                "internalType": "address",
                "name": "tokenB",
                "type": "address"
                },
            ],
			"name": "getReserves",
			"outputs": [
				{
					"internalType": "uint",
					"name": "reserveA",
					"type": "uint"
				},
				{
					"internalType": "uint",
					"name": "reserveB",
					"type": "uint"
				}
			],
			"stateMutability": "view",
			"type": "function"
		}
	]

# Contrat intermédiaire
address = "0x763B7c443a97C4f075b419cbe061095CB89B3A8B"

contract = w3.eth.contract(address=address, abi=abi)
contract.all_functions()

contract.functions.getReserves(
    "0x5C69bEe701ef814a2B6a3EDD4B1652CB9cc5aA6f",
    "0xbb76889A512Bd0E017226E3976A6cEb37647B887",
    "0xc1C0472c0C80bCcDC7F5D01A376Bd97a734B8815").call()

