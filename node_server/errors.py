from flask import abort

def abort_with_invalid_address(address):
    abort(400, "The following address does not contain a valid address format: {}".format(address))