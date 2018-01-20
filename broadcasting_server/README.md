# Broadcasting Server

The following module is designed to listen out for new transactions and broadcast them to existing nodes on the network.

## TODO list 

- Set up sockets for Flask
- Setup channels to listen and broadcast messages

## How to run broadcasting server 

Run the following command to start up a gunicorn worker: 

`gunicorn -k flask_sockets.worker main:app`

In another window, start the server by typing:

`python main.py`



## Extras

To make a new state, run: 

`python make_new_state.py`
