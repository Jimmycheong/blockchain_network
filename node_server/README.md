# Node Server

The following module contains code to run a node server in the blockchain network. 

Responsibilities of a node server:
- Listen for new transactions on endpoints
- Verify transactions using existing state.
- Create new blocks (from new transactions) to append to the existing blockchain.
- Send the information to the broadcast server to be announced across the network.
- Receive the most updated blockchain to be mined.

Run the server with the addition of a specified port: 

`flask run --port 7000`



Once a node has recorded sufficient number of transactions, the transactions can be submitted
to the broadcasting server to create a new block to be appended onto the global blockchain

`python submit_block.py`


To check whether the blockchain found in the resources folder is valid, run:

`python validate_blockchain.py`