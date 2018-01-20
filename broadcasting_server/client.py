'''client.py

https://anaconda.org/pypi/websocket-client

CURRENT STATUS: WORK IN PROGRESS:

TODO: 
- Open up a socket connection to allow clients to connect to 
- Send the latest blockchain information to connected clients.

'''

from websocket import create_connection
ws = create_connection("ws://localhost:8000/echo")
print ("Sending 'Hello, World'...")
ws.send("Hello, World")
print ("Sent")
print ("Reeiving...")

try:
    while True:
        result =  ws.recv()
        print ("Received '%s'" % result)
except KeyboardInterrupt:
    pass

ws.close()