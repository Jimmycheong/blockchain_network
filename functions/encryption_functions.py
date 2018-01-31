import base58
from Crypto.Hash import SHA256
from Crypto.Hash.RIPEMD import RIPEMD160Hash
from ecdsa import SigningKey, SECP256k1

def generate_ecdsa_keypair():
    '''
    Generates a public and private keypair using ECDSA
    '''
    sk = SigningKey.generate(curve=SECP256k1)
    vk = sk.get_verifying_key()

    return sk, vk

def generate_public_address(public_key):
    '''
    Generates a public Base58 encoded address using SHA-256
    and RIPEMD-160 hashing algorithms. 

    Params: 
        public_key (bytes): Byte string of the public key

    Returns: (str) Base58 hash of the public address

    '''

    if len(public_key) != 64: 
        raise Exception("Please enter a")

    hash_1 = SHA256.new(public_key).hexdigest() # Stage 1 
    r160_hash_obj = RIPEMD160Hash() # Stage 2
    r160_hash_obj.update(hash_1)    
    hash_2 = r160_hash_obj.hexdigest()
    hash_3 = "00" + hash_2 # Stage 3 

    checksum = generate_checksum(hash_3) # Stage 4
    bit_address = hash_3 + checksum # Stage 5
    
    return base58.b58encode(bytes.fromhex(bit_address)) # Stage 6

def generate_checksum(hash_1): 
    '''
    Params: 
        hash_1 (str): Hexidecimal string

    Returns: Checksum of the hash
    '''

    hash_2 = SHA256.new(str.encode(hash_1)).digest().hex() 
    hash_3 = SHA256.new(str.encode(hash_2)).digest() 
    return hash_3[:4].hex() # Checksum


def is_valid_public_address(public_address): 
    '''Checks to see if an address is a valid address

    public_address (str): A base58 string to be decoded 

    Returns: Boolean stating whether the public address has a valid format
    '''
    binary_addr = base58.b58decode(pub_addr)
    checksum = binary_addr[-4:].hex()    
    if checksum == generate_checksum(binary_addr[:-4].hex()):
        return True
    else:
        return False

