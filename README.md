# Blockchain Network
A mini-project aimed at building a blockchain network. 

## Modules

`broadcasting_server`: 
- Listens for new blocks
- Broadcasts new chains to all connected clients

`node_server`: 
- Listens for new transactions 
- Listens for the latest version of the blockchain
- Creates new blocks from new transactions
- Sends new blocks to be appended to the latest blockchain


## How to setup project

Install all dependancies on each module using the pip command line tool: 

`pip install -r requirements.txt`

To create the genesis block: 

`python create_genesis.py`

To check whether the latest block is valid: 

`python check_block.py`