''' send_coins.py

This script is used to send coins from one address to another by creating
a new transactions to be broadcasted across all nodes on the network.

'''

import os
import sys
sys.path.append("..")

from ecdsa import SigningKey, SECP256k1
from functions.encryption_functions import (
    generate_public_address,
    is_valid_public_address
)

RECEIVER_ADDR = '1BWe4MvDUeq7yjsP5PcR64c85xAPm2spEa'
amount = 50

def create_new_transaction(sender_addr, receiver_addr, amount):

    '''
    TODO: Implement real logic

    - Creates a new transaction
    - Sends transactions to a HTTP endpoint on a node server

    Params:
        sender_addr(str) : Base58encoded public address of the sender 
        receiver_addr(str) : Base58encoded public address of the receiver
        amount(int) : Amount to send from the sender to the receiver
    '''

    print("""
        SENDER: {}
        RECEIVER: {}
        AMOUNT: {}
    """.format(sender_addr, receiver_addr, amount))


def main():

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

    print("Sender address: {}".format(SENDER_ADDR))

    if not is_valid_public_address(RECEIVER_ADDR): 
        raise Exception("Receiver address does not have a valid address format.")

    create_new_transaction(SENDER_ADDR, RECEIVER_ADDR, amount)

if __name__ == "__main__":
    main()