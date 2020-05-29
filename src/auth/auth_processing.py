import hashlib
import sys
from src.config import salt


def encrypt_string(hash_string):
    hash_string += salt
    sha_signature = hashlib.sha256(hash_string.encode()).hexdigest()
    return sha_signature