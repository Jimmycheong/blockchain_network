''' validate_blockchain.py

The following file is used to check whether the blockchain file 
found within the resources folder is valid.

'''
import os
import sys
sys.path.append("..")
from validity_functions import checkChain

from functions import read_from_pickle
from pprint import pprint

def main():

    if not os.path.exists("resources/chain.pkl"):
        raise Exception("'resources/chain.pkl' does not exist") 

    chain = read_from_pickle("resources/chain.pkl")
    state = checkChain(chain)

if __name__ == '__main__':
    main()