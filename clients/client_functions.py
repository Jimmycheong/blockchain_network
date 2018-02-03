import sys
sys.path.append("..")

from constants import LINE
import requests

def create_new_transaction(sender_addr, receiver_addr, amount):

    '''
    TODO: Implement real logic

    - Creates a new transaction
    - Sends transactions to a HTTP endpoint on a node server

    Params:
        sender_addr(str) : Base58encoded public address of the sender 
        receiver_addr(str) : Base58encoded public address of the receiver
        amount(int) : Amount to send from the sender to the receiver
        
    Returns: A dictionary representing the transaction details between the two parties.
    '''
    return {sender_addr: -1 * amount,receiver_addr: amount}


def send_transaction_to_server(server_addr, txn):

    '''

    Params:
        server_addr(str): The address of the node server to send the transaction to
        txn (dict): The transaction to post to the node server

    Returns: 
        resp(response): requests response object from the node server
    '''

    try: 
        resp = requests.post(server_addr, json=txn)
    except Exception as e:
        print("No response from server.") 
    return resp

def print_failed_response(resp):
    '''
    Prints a message to the terminal following an unsuccessful HTTP request call
        
    Params:
        resp(response): response object from 'requests' library
    '''
    print("""
    {}
    FAILURE: Failed to post new transaction to node server
    {}
    Response message: {}
    """.format(LINE, LINE, resp.text))


def print_success_response():
    '''
    Print a message displaying success a successful HTTP request call
    '''
    print("""
    {}
    SUCCESS: New transaction received by the node server.
    {}""".format(LINE, LINE))


