import sys
sys.path.append("..")

from functions import (
    read_from_pickle,
    save_to_pickle
)
from validity_functions import checkChain

def main():

    chain = read_from_pickle("resources/chain.pkl")

    state = checkChain(chain)

    save_to_pickle("resources/latestState.pkl", state)


if __name__ == '__main__':
    main()