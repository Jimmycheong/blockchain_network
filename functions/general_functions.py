'''Function.py

A collection of functions used in this project

'''

import hashlib
import json
import pickle
import random
import sys

random.seed(0)

def update_state(tokens, state):

    # --------------------TODO--------------------

    # Inputs: tokens, state: dictionaries keyed with account names, holding numeric values for transfer amount (tokens) or account balance (state)
    # Returns: Updated state, with additional users added to state if necessary
    # NOTE: This does not not validate the transaction- just updates the state!
    
    # If the transaction is valid, then update the state
    state = state.copy() # As dictionaries are mutable, let's avoid any confusion by creating a working copy of the data.
    for key in tokens:
        if key in state.keys():
            state[key] += tokens[key]
        else:
            state[key] = tokens[key]
    return state

def make_block(tokens, chain):

    '''
    Inputs: 
        token(list)): A list of transaction objects (dictionary objects)
        chain (list): The blockchain containing the blocks (dicts)

    Returns: A dictionary representing the hash to be appended to the chain
    '''
    parent_block = chain[-1]

    block_header = {
        u'blockNumber':parent_block[u'contents'][u'blockNumber'] + 1,
        u'parentHash':parent_block[u'hash'],
        u'tokenCount':len(tokens),
        u'tokens':tokens
    }

    block_hash = hash_function(block_header)
    
    return {u'hash':block_hash,u'contents':block_header}

def save_to_pickle(directory, data):
    '''Saves a python object as a pickle file'''

    with open(directory, 'wb') as file:
        pickle.dump(data, file)

def read_from_pickle(directory): 
    '''
    Reads a pickle file 

    Returns: 
        loaded_obj(any): returns the object loaded from the pickle file.
    '''
    with open(directory, 'rb') as file:
        loaded_obj = pickle.load(file)

    return loaded_obj

def create_genesis_block(creator_addr, initial_amount):
    '''
    Creates initial block of chain sequence

    Params:
        creator_addr(str): base58 public address
        initial_amount(int): Initial amount of tokens to create. Fixed amount.

    Returns: 
        genesis_block (dict): The initial block to be append to the chain
    '''

    state = {u"{}".format(creator_addr): initial_amount}  # Initial state
    genesis_block_tokens = [state]
    genesis_block_contents = {u'blockNumber':0,u'parentHash':None,u'tokenCount':1,u'tokens':genesis_block_tokens}
    genesis_hash = hash_function(genesis_block_contents)
    genesis_block = {u'hash':genesis_hash,u'contents':genesis_block_contents}

    return genesis_block

def hash_function(header=""):
    '''
    Hashes a block header (information about the block) to return a digest

    Input: 
        header(dict): contains information regarding the block

    Returns: A 32-bit digest using SHA256

    '''

    # For convenience, this is a helper function that wraps our hashing algorithm
    if type(header)!=str:
        header = json.dumps(header,sort_keys=True)  
        
    if sys.version_info.major == 2:
        return unicode(hashlib.sha256(header).hexdigest(),'utf-8')
    else:
        return hashlib.sha256(str(header).encode('utf-8')).hexdigest()


def make_transaction(maxValue=3):
    '''
    --------------------TODO--------------------

    Used to generate random transactions
    '''
    # This will create valid transactions in the range of (1,maxValue)
    sign      = int(random.getrandbits(1))*2 - 1   # This will randomly choose -1 or 1
    amount    = random.randint(1,maxValue)
    jimmy_pays = sign * amount
    alice_pays   = -1 * jimmy_pays
    # By construction, this will always return transactions that respect the conservation of tokens.
    # However, note that we have not done anything to check whether these overdraft an account
    return {u'Jimmy':jimmy_pays,u'Alice':alice_pays}


def is_valid_token(token,state):
    '''
    Confirms whether the token's transactions are valid for processing

    Inputs:
        token(dict): A dictionary containing transaction between parties
        state(dict): The current state of all funds aggregated on the blockchain

    Returns: Boolean to validate the legitimacy of the token
    '''

    # Check that the sum of the deposits and withdrawals is 0
    if sum(token.values()) is not 0:
        return False
    
    # Check that the transaction does not cause an overdraft
    for user_key in token.keys():
        if user_key in state.keys(): 
            account_balance = state[user_key]
        else:
            account_balance = 0

        if (account_balance + token[user_key]) < 0:
            return False
    
    return True