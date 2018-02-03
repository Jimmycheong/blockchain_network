'''validate_blockchain.py

The following file checks to see if a blockchain is valid
'''

from functions.validity_functions import checkChain
from functions.general_functions import (read_from_json, save_to_json)
from pprint import pprint

from constants import CHAIN_DIR, LATEST_STATE_DIR

def main():

    chain = read_from_json("resources/{}".format(CHAIN_DIR))

    print("\nChain:\n")
    pprint(chain)

    state = checkChain(chain)

    print("\nThe blockchain is valid!\n\nState:\n{}".format(state))

    save_to_json("resources/{}".format(LATEST_STATE_DIR), state)

    print("Latest state saved as pickle file.")

if __name__ == '__main__':
    main()