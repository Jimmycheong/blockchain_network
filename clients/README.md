# Clients 

Each new user who wishes to use this technology requires a keypair consisting of a public address and a private key. 

The public address represents the destination to which other users can send coins to.

The private key is used to gain access to the wallet. This is acheived by creating new transactions which can be digitally signed using the private key. 

The private key should be kept secret and stored safely by the user who created the keypair.

To create a new keypair, run the script: 

`python create_keypair.py`


To send coins to another address, ensure: 
- A private key file exists in the 'keys' folder
- The address to send coins to is valid.

Then run the following script: 
`python send_coins.py`