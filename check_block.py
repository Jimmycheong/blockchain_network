'''validate_blockchain.py

The following file checks to see if a blockchain is valid
'''

from functions.validity_functions import checkChain
from functions.general_functions import (read_from_pickle, save_to_pickle)
from pprint import pprint

def main():

    chain = read_from_pickle("resources/chain.pkl")

    print("\nChain:\n")
    pprint(chain)

    state = checkChain(chain)

    print("\nThe blockchain is valid!\n\nState:\n{}".format(state))

    save_to_pickle("resources/latestState.pkl", state)

    print("Latest state saved as pickle file.")

if __name__ == '__main__':
    main()