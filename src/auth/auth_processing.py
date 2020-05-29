import hashlib
from src.config import salt
import sqlalchemy


class AuthProcessing:
    def __init__(self, engine):
        self.engine = engine

    @staticmethod
    def encrypt_string(hash_string):
        hash_string += salt
        sha_signature = hashlib.sha256(hash_string.encode()).hexdigest()
        return sha_signature

    def auth_user(self, login, hash):
        query = "SELECT id FROM users WHERE account='" + login + "' AND hash='" + hash + "';"

        print(query)
        with self.engine.connect() as con:
            rs = con.execute(query)

            print("A")
            for row in rs:
                print(row)
            print("B")