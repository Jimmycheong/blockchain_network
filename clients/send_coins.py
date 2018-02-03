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
    is_valid_public_address,
)
from constants import LINE

from functions.general_functions import is_valid_input_amount

from client_functions import (
    create_new_transaction, 
    send_transaction_to_server,
    print_failed_response,
    print_success_response
)

RECEIVER_ADDR = '1BkvDiMc9SgoDK7BY1Vpg9ee2rYb3uy7tn' # Remove in prod

NODE_SERVER_ADDRESS = "http://localhost:7005/api/transaction/new"

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
    str_amount = input("Enter an amount of coins to send: ")

    # if len(user_input) == 0: 
    #     print("\nNo address entered. Exiting...")
    #     sys.exit(0)

    if not is_valid_input_amount(str_amount) or len(str_amount) == 0:
        raise ValueError('"{}" is not a valid amount to send. Try again.'.format(str_amount))

    amount = int(str_amount)

    if amount <= 0: 
        print("\nInvalid amount. Exiting...")
        sys.exit(0)

    user_input = RECEIVER_ADDR # Remove in prod.

    if not is_valid_public_address(RECEIVER_ADDR): 
        raise Exception("Receiver address does not have a valid address format.")

    new_txn = create_new_transaction(SENDER_ADDR, RECEIVER_ADDR, amount)

    resp = send_transaction_to_server(NODE_SERVER_ADDRESS, new_txn)

    if resp.status_code == 200: 
        print_success_response()
    else:
        print_failed_response(resp)

    print("""
    SENDER: {}
    RECEIVER: {}
    AMOUNT: {}
    """.format(SENDER_ADDR, RECEIVER_ADDR, amount))

if __name__ == "__main__":
    main()