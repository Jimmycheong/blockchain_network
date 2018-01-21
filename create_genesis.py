''' blockchain_generator.py

The following file is used to generate a new blockchain and stores it locally as a pickle file.

''' 

from functions import create_genesis_block, save_to_pickle

def main():

    gb = create_genesis_block()
    chain = [gb] # Create the blockchain

    save_to_pickle("resources/chain.pkl", chain)
    print("New Blockchain created..")

if __name__ == '__main__':
    main()