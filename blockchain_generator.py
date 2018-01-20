''' blockchain_generator.py

The following file is used to generate a new blockchain and stores it locally as a pickle file.

''' 

from functions import (
    create_genesis_block,
    save_to_pickle
)

def main():

    print("Creating genesis block..")
    gb = create_genesis_block()

    print("Creating the new chain...")
    chain = [gb] # Create the blockchain

    print("Saving new chain as pickle file....")
    save_to_pickle("resources/chain.pkl", chain)


if __name__ == '__main__':
    main()