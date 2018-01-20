import sys
sys.path.append("..")

import json 
import requests
import os

from functions import make_block

def clear_existing_transactions_file(file_path='resources/existingTransactions.json'):

    existing_transactions = []

    with open(file_path, 'w+', encoding="utf8") as file:
        json.dump(existing_transactions, file)


def update_existing_transactions_file(existing_transactions, file_path='resources/existingTransactions.json'):

    '''
    Updates the JSON file containing all existing transaction.

    Inputs: 
        existing_transactions(list): A list of the latest transactions to write
        (Optional) file_path (str): The path to the JSON file containing the existing transactions

    '''

    if type(existing_transactions) != list:
        raise TypeError("expected list, not type{}".format(type(existing_transactions)))

    with open(file_path, 'w+', encoding="utf8") as file:
        json.dump(existing_transactions, file)


def get_existing_transactions(file_path="resources/existingTransactions.json"):

    '''
    Reads from the node server's local resource folder the grab all existing transactions found
    in the JSON file.

    Inputs:
        (Optional) file_path (str): The path to the JSON file containing the existing transactions

    '''

    if not os.path.exists(file_path):
        existing_transactions = []
        with open(file_path, 'w+', encoding="utf8") as file:
            json.dump(existing_transactions, file)

    with open(file_path, 'r') as file:
        existing_transactions = json.load(file)
    
    return existing_transactions


def submit_new_block_to_blockchain(remote_host, tokens, chain): 

    '''
    Submit new block to remote broadcasting server

    Inputs: 
        remote_host(str): The IP address of the remote broading server
        tokens(list): A list of transactions (dict)
        chain (list): The most up-to-date blockchain

    '''

    new_block = make_block(tokens, chain)

    res = requests.post(
        'http://localhost:5000/api/blockchain/append', 
        json=new_block
    )

    print("Response msg: ", res.text)

    if res.status_code != 200: 
        raise Error("Bad request!")
