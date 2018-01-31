import sys
sys.path.append("..")

from functions.encryption_functions import (
    generate_ecdsa_keypair,
    generate_public_address
)


def main():
    
    sign_key, verify_key = generate_ecdsa_keypair()

    sign_key_byte = sign_key.to_string()
    verify_key_byte = verify_key.to_string()

    public_address = generate_public_address(verify_key_byte)

    print("""
        Created keypair in directory 'keys'!
        Please keep the private key safe.
        The public key is used as part of transactions to verify the validity 
        of a transactions.
        
        To receive money from someone, please give them your public address:
        "{}"
        """.format(public_address)
    )

    with open("keys/public_address.key", "w") as file:
        file.write(public_address)

    with open("keys/private.key", "w") as file:
        file.write(verify_key_byte.hex())

if __name__ == '__main__':
    main()