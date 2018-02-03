''' validate_blockchain.py

The following file is used to check whether the blockchain file 
found within the resources folder is valid.

'''
import os
import sys
sys.path.append("..")
from functions.validity_functions import checkChain

from functions.general_functions import read_from_pickle
from pprint import pprint

from constants import CHAIN_DIR

def main():

    if not os.path.exists("resources/{}".format(CHAIN_DIR)):
        raise FileNotFoundError("'resources/{}' does not exist".format(CHAIN_DIR)) 

    chain = read_from_pickle("resources/{}".format(CHAIN_DIR))
    state = checkChain(chain)

    if not state: 
        print("The chain is not valid")
    else: 
        print("The chain file is valid for use!")

if __name__ == '__main__':
    main()
