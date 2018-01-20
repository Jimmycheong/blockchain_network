'''main.py

The purpose of this file is to run a node server with endpoint functionality. 
It allows for new users to create transactions which can then be appended onto the 
blockchain and sent to the broadcast server.

'''

import sys
sys.path.append("..")

from flask import Flask, request, abort
import json
from pprint import pprint 
import requests

# Imports from package above
from functions import is_valid_token, read_from_pickle, make_block
from validity_functions import checkChain

from .node_functions import (
    update_existing_transactions_file, 
    get_existing_transactions
)


app = Flask(__name__)
app.port = 7000

@app.route("/api/balance/<account_holder>",  methods=['GET'])
def check_balance(account_holder):

    chain = read_from_pickle("resources/chain.pkl")
    state = checkChain(chain)

    if account_holder in state.keys():
        return "{} has {} in their account".format(account_holder, state[account_holder])
    else: 
        return "{} does not exist and therefore does not have any money on their account".format(account_holder)

@app.route("/api/transaction/new",  methods=['POST'])
def add_new_transactions():

    token = request.get_json()
    chain = read_from_pickle("resources/chain.pkl")
    state = checkChain(chain)

    if not is_valid_token(token, state):
        abort(400, "Transaction is not valid")

    existing_transactions = get_existing_transactions()
    existing_transactions.append(token)

    update_existing_transactions_file(existing_transactions)

    return "Transaction successfully added"
