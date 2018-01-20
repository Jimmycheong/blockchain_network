'''submit_block.py

The following script is used by a client to submit new blocks 
a broadcasting server to build the new blockchain

Process: 
- Reads the json file containing a list of all existing transactions
    to be processed
- Ensures number of tokens inside are not exceeded.
- Hits the endpoint of the broadcasting server to create new block

'''
import sys
sys.path.append("..")

import os
import json

from functions import (
    is_valid_token,
    read_from_pickle,
    make_block
)
from validity_functions import checkChain
from node_functions import submit_new_block_to_blockchain

def main():

    file_path = "resources/existingTransactions.json"

    if not os.path.exists(file_path):
        raise FileNotFoundError("Cannot locate {}".format(file_path))

    with open(file_path, 'r') as file:
        existing_transactions = json.load(file)

    if type(existing_transactions) != list:
        raise TypeError("expected list, not type{}".format(type(existing_transactions)))


    # Validation Check 
    chain = read_from_pickle("resources/chain.pkl")
    state = checkChain(chain)

    for et in existing_transactions:
        if not is_valid_token(et, state):
            raise Exception("Token invalid : {}")

    print("All tokens valid.")

    # Submit block for appending to global chain
    submit_new_block_to_blockchain(
        'http://localhost:5000/api/blockchain/append',
        existing_transactions, 
        chain
    )

    print("Successfully submitted block..")

if __name__ == '__main__':
    main()

