import sys
sys.path.append("..")

from functions.general_functions import (
    read_from_json,
    save_to_json
)
from validity_functions import checkChain
from constants import CHAIN_DIR, LATEST_STATE_DIR

def main():

    chain = read_from_json("resources/{}".format(CHAIN_DIR))
    state = checkChain(chain)
    save_to_json("resources/{}".format(LATEST_STATE_DIR), state)

if __name__ == '__main__':
    main()