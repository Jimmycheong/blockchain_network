# Node Server

The following module contains code to run a node server in the blockchain network. 

Responsibilities of a node server:
- Listen for new transactions on endpoints
- Verify transactions using existing state.
- Create new blocks (from new transactions) to append to the existing blockchain.
- Send the information to the broadcast server to be announced across the network.
- Receive the most updated blockchain to be mined.
