'''main.py

The responsbilities of this file are: 
- Listen for nodes 
- Create new a blockchain from verified transactions
- Broadcast new blockchain to all clients

Before running this server, ensure a gunicorn worker is run as a broker
for the websockets, by typing into the seperate terminal

gunicorn -k flask_sockets.worker main:app

'''

import sys
sys.path.append("..")

from constants import *

from flask import (
    Flask,
    request,
    abort
)
from flask_sockets import Sockets
import json


# Functions from package above
from validity_functions import check_block_validity
from functions import (
    read_from_pickle,
    save_to_pickle
)

app = Flask(__name__)
sockets = Sockets(app)

@app.route("/api/blockchain",  methods=['GET'])
def get_newest_version_of_blockchain():
    print("Called")
    chain = read_from_pickle("resources/chain.pkl")
    return json.dumps(chain)


@app.route("/api/blockchain/append", methods=['POST'])
def verify_and_append_new_block():
    try: 
        data = request.get_json()
    except:
        abort(400, "Submitted data is not JSON format")

    if (type(data)) != dict:
        abort(400, "Data is not in list format")

    state = read_from_pickle("resources/latestState.pkl")
    chain = read_from_pickle("resources/chain.pkl")

    parent_block = chain[-1]

    if not check_block_validity(data, parent_block, state): 
        abort(400, "Block is not valid")

    print("Reached 3!")
    chain.append(data)

    # TODO: SAVE BLOCK and Broadcast
    # save_to_pickle("resources/chain.pkl", chain)    

    return json.dumps(chain)


'''
Web Sockets
'''

@sockets.route('/echo')
def echo_socket(ws):
    clients = []
    if ws not in clients:
        clients.append(ws)

    print("Client list length: ", len(clients))

    while not ws.closed:
        message = ws.receive()
        ws.send(message)


if __name__ == "__main__":
    app.run(debug=True)
    # from gevent import pywsgi
    # from geventwebsocket.handler import WebSocketHandler
    # server = pywsgi.WSGIServer(('', 5000), app, handler_class=WebSocketHandler)
    
    # print("Sever started on localhost:5000")

    # server.serve_forever()