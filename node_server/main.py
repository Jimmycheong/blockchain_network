'''main.py

The purpose of this file is to run a node server with endpoint functionality. 
It allows for new users to create transactions which can then be appended onto the 
blockchain and sent to the broadcast server.

'''

import sys
sys.path.append("..")

from flask import Flask, request
from functions import is_valid_token, read_from_pickle, make_block
from validity_functions import checkChain

app = Flask(__name__)

@app.route("/api/balance/<account_holder>",  methods=['GET'])
def validate_transaction(account_holder):

    chain = read_from_pickle("resources/chain.pkl")
    state = checkChain(chain)

    if account_holder in state.keys():
        return "{} has {} in their account".format(account_holder, state[account_holder])
    else: 
        return "{} does not exist and therefore does not have any money on their account".format(account_holder)

@app.route("/api/transaction/new",  methods=['POST'])
def add_new_transactions():

    print(request.get_json())
    token = request.get_json()

    chain = read_from_pickle("resources/chain.pkl")

    state = checkChain(chain)

    result = is_valid_token(token, state)

    new_block = make_block([token], chain)

    chain.append(new_block)

    print("New block:\n", chain)

    return "Transaction valid? : {}".format(result)

