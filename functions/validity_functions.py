from .general_functions import (
    hash_function,
    update_state,
    is_valid_token
)

from constants import MINIMUM_NUMBER_OF_TRANSACTIONS

def check_block_hash(block):

    # --------------------TODO--------------------

    # Raise an exception if the hash does not match the block contents
    expectedHash = hash_function( block['contents'] )
    if block['hash']!=expectedHash:
        raise Exception('Hash does not match contents of block %s'%
                        block['contents']['blockNumber'])
    return

def check_block_validity(block,parent,state):  

    # --------------------TODO--------------------

    # We want to check the following conditions:
    # - Each of the transactions are valid updates to the system state
    # - Block hash is valid for the block contents
    # - Block number increments the parent block number by 1
    # - Accurately references the parent block's hash

    parent_number = parent['contents']['blockNumber']
    parent_hash   = parent['hash']
    block_number  = block['contents']['blockNumber']


    if len(block['contents']['tokens']) < MINIMUM_NUMBER_OF_TRANSACTIONS:
        raise Exception("Not enough transations to make a block. Minimum number: 4")
    
    # Check transaction validity; throw an error if an invalid transaction was found.
    for txn in block['contents']['tokens']:
        if is_valid_token(txn,state):
            state = update_state(txn,state)
        else:
            raise Exception('Invalid transaction in block %s: %s'%(block_number,txn))

    check_block_hash(block) # Check hash integrity; raises error if inaccurate

    if block_number!=(parent_number+1):
        raise Exception('Hash does not match contents of block %s'%block_number)

    if block['contents']['parentHash'] != parent_hash:
        raise Exception('Parent hash not accurate at block %s'%block_number)
    
    return state

def checkChain(chain):

    # --------------------TODO--------------------

    # Work through the chain from the genesis block (which gets special treatment), 
    #  checking that all transactions are internally valid,
    #    that the transactions do not cause an overdraft,
    #    and that the blocks are linked by their hashes.
    # This returns the state as a dictionary of accounts and balances,
    #   or returns False if an error was detected

    
    ## Data input processing: Make sure that our chain is a list of dicts
    if type(chain)==str:
        try:
            chain = json.loads(chain)
            assert( type(chain)==list)
        except:  # This is a catch-all, admittedly crude
            return False
    elif type(chain)!=list:
        return False
    
    state = {}
    ## Prime the pump by checking the genesis block
    # We want to check the following conditions:
    # - Each of the transactions are valid updates to the system state
    # - Block hash is valid for the block contents

    for txn in chain[0]['contents']['tokens']:
        state = update_state(txn,state)
    check_block_hash(chain[0])
    parent = chain[0]
    
    ## Checking subsequent blocks: These additionally need to check
    #    - the reference to the parent block's hash
    #    - the validity of the block number
    for block in chain[1:]:
        state = check_block_validity(block,parent,state)
        parent = block
        
    return state