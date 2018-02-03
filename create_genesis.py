''' blockchain_generator.py

The following file is used to generate a new blockchain and stores it locally as a pickle file.

''' 

from functions.general_functions import (
    create_genesis_block, 
    save_to_json
)

from constants import CHAIN_DIR

def main():

    CREATOR_ADDR = "1PSVg4fkepzn8htNLPG3S9dUS8hLtxa7Fu"
    INITIAL_AMOUNT = 1000000000

    chain_name = input("\nEnter a filename for chain(default:{}): ".format(CHAIN_DIR))

    if len(chain_name) == 0: 
        chain_name = CHAIN_DIR

    gb = create_genesis_block(CREATOR_ADDR, INITIAL_AMOUNT)
    chain = [gb] # Create the blockchain

    save_to_json("resources/{}".format(chain_name), chain)
    print("""
        #--------##--------##--------##--------#
        New Blockchain created!
        #--------##--------##--------##--------#
        Creator address: {}
        Initial amount created: {}
        Save location: resources/{}
        #--------##--------##--------##--------#

        """.format(
                CREATOR_ADDR, 
                INITIAL_AMOUNT, 
                chain_name
        ))

if __name__ == '__main__':
    main()