''' send_coins.py

This script is used to send coins from one address to another by creating
a new transactions to be broadcasted across all nodes on the network.

'''

import os
import sys
sys.path.append("..")

import base58
import json
from ecdsa import SigningKey, SECP256k1
import requests

from functions.encryption_functions import (
    generate_public_address,
    is_valid_public_address
)

RECEIVER_ADDR = '1BkvDiMc9SgoDK7BY1Vpg9ee2rYb3uy7tn'
amount = 50

NODE_SERVER_ADDRESS = "http://localhost:7005/api/transaction/new"

def create_new_transaction(sender_addr, receiver_addr, amount):

    '''
    TODO: Implement real logic

    - Creates a new transaction
    - Sends transactions to a HTTP endpoint on a node server

    Params:
        sender_addr(str) : Base58encoded public address of the sender 
        receiver_addr(str) : Base58encoded public address of the receiver
        amount(int) : Amount to send from the sender to the receiver
        
    Returns: A dictionary representing the transaction details between the two parties.
    '''
    return {sender_addr: -1 * amount,receiver_addr: amount}


def send_transaction_to_server(server_addr, txn):

    '''

    Params:
        server_addr(str): The address of the node server to send the transaction to
        txn (dict): The transaction to post to the node server

    Returns: 
        resp(response): requests response object from the node server
    '''

    try: 
        resp = requests.post(server_addr, json=txn)
    except Exception as e:
        print("No response from server.") 
    return resp


def main():

    # Checks if private key exists
    if not os.path.exists("keys/private.key"):
        raise FileNotFoundError("Cannot find the file: keys/private.key. Please supply a private key.")

    with open("keys/private.key", 'r') as file:
        sk_hex = file.read()

    try: 
        sk = SigningKey.from_string(bytes.fromhex(sk_hex), curve=SECP256k1)
    except:
        raise Exception("Invalid private key file. Please try again.")

    vk = sk.get_verifying_key()
    SENDER_ADDR = generate_public_address(vk.to_string())

    print("\nSender address: {}".format(SENDER_ADDR))

    user_input = input("Enter an address to send coins to: ")
    input_amount = input("Enter an amount of coins to send: ")

    # Include in prod.
    # if len(user_input) == 0: 
    #     print("\nNo address entered. Exiting...")
    #     sys.exit(0)

    # Include in prod.
    # if len(input_amount) < 0: 
    #     print("\nInvalid amount. Exiting...")
    #     sys.exit(0)

    user_input = RECEIVER_ADDR # Remove in prod.
    input_amount = amount # Remove in prod.

    if not is_valid_public_address(RECEIVER_ADDR): 
        raise Exception("Receiver address does not have a valid address format.")

    new_txn = create_new_transaction(SENDER_ADDR, RECEIVER_ADDR, input_amount)

    resp = send_transaction_to_server(NODE_SERVER_ADDRESS, new_txn)

    if resp.status_code == 200: 
        print("\nSUCCESS! Succeeded with posting the following transaction: ")
    else:
        print("\nFAILURE: Failed to post new transaction to node server: ")

    print("""
        SENDER: {}
        RECEIVER: {}
        AMOUNT: {}
    """.format(SENDER_ADDR, RECEIVER_ADDR, input_amount))

if __name__ == "__main__":
    main()