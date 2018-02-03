'''main.py

The purpose of this file is to run a node server with endpoint functionality. 
It allows for new users to create transactions which can then be appended onto the 
blockchain and sent to the broadcast server.

'''

import sys
sys.path.append("..") # Enables access to parent modules

from flask import Flask, request, abort
import json
from pprint import pprint 
import requests

from constants import CHAIN_DIR

from functions.general_functions import is_valid_token, make_block, read_from_json
from functions.validity_functions import checkChain
from functions.encryption_functions import is_valid_public_address 

from .node_functions import (
    update_existing_transactions_file, 
    get_existing_transactions,
    update_state_with_existing_transactions
)

from .errors import abort_with_invalid_address

app = Flask(__name__)
app.port = 7005

@app.route("/api/balance/<account_holder>",  methods=['GET'])
def check_balance(account_holder):

    if not is_valid_public_address(account_holder):
        abort_with_invalid_address(account_holder)

    chain = read_from_json("resources/{}".format(CHAIN_DIR))
    state_of_chain = checkChain(chain)

    existing_txns = get_existing_transactions()
    latest_state = update_state_with_existing_transactions(state_of_chain, existing_txns)     

    if account_holder in latest_state.keys():
        return "{} has {} in their account".format(account_holder, latest_state[account_holder])
    else: 
        return "{} does not exist and therefore does not have any money on their account".format(account_holder)


@app.route("/api/transaction/new",  methods=['POST'])
def add_new_transactions():

    txn = request.get_json()

    print("Received transactions:", txn)

    #Checks if all addresses are in correct format
    for address in txn.keys():
        if not is_valid_public_address(address):
            abort_with_invalid_address(address)

    chain = read_from_json("resources/{}".format(CHAIN_DIR))
    state_of_chain = checkChain(chain)

    existing_txns = get_existing_transactions()
    latest_state = update_state_with_existing_transactions(state_of_chain, existing_txns) 

    if not is_valid_token(txn, latest_state):
        abort(400, "Transaction is not valid")

    existing_txns.append(txn)
    update_existing_transactions_file(existing_txns)

    return "Transaction successfully added"
