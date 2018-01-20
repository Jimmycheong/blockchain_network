''' blockchain_generator.py

The following file is used to generate a new blockchain and stores it locally as a pickle file.

''' 

from functions import (
    create_genesis_block,
    save_to_pickle,
    make_transaction,
    make_block
)

def main():

    gb = create_genesis_block()
    chain = [gb] # Create the blockchain

    # Generate a list of transactions
    list_of_transactions = [make_transaction() for i in range(5)]

    for transaction in list_of_transactions:
        print(transaction)

    new_block = make_block(list_of_transactions, chain)
    chain.append(new_block)

    save_to_pickle("resources/chain.pkl", chain)
    print("New Blockchain created..")


if __name__ == '__main__':
    main()