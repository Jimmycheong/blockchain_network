# Blockchain Network

A project to build a blockchain technology that uses transactions of virtual currency. Uses node servers to listen for new transactions and broadcasting servers to broadcast the latest block to all network nodes.

## Modules

### [broadcasting_server](/broadcasting_server)
- Listens for new blocks
- Broadcasts new chains to all connected clients

### [node_server](/node_server)
- Listens for new transactions 
- Listens for the latest version of the blockchain
- Creates new blocks from new transactions
- Sends new blocks to be appended to the latest blockchain

### [clients](/clients)
- Allows new users to generate a public address and private key
- Allows users to create new transactions to other users.

## How to setup the project

Install all dependancies on each module using the pip command line tool: 

`pip install -r requirements.txt`

To create the genesis block: 

`python create_genesis.py`

To check whether the latest block is valid: 

`python check_block.py`
