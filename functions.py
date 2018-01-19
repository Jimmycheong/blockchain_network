import hashlib, json, sys
import random
random.seed(0)


def create_genesis_block():
    '''
    Creates initial block of chain sequence

    Returns: 
        genesis_block (dict): The initial block to be append to the chain
    '''

    state = {u"Jimmy": 100000, u"Alice":50}  # Initial state
    genesis_block_tokens = [state]
    genesis_block_contents = {u'blockNumber':0,u'parentHash':None,u'txnCount':1,u'txns':genesis_block_tokens}
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
    # This will create valid transactions in the range of (1,maxValue)
    sign      = int(random.getrandbits(1))*2 - 1   # This will randomly choose -1 or 1
    amount    = random.randint(1,maxValue)
    alicePays = sign * amount
    bobPays   = -1 * alicePays
    # By construction, this will always return transactions that respect the conservation of tokens.
    # However, note that we have not done anything to check whether these overdraft an account
    return {u'Alice':alicePays,u'Bob':bobPays}


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