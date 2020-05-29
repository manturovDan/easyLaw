import hashlib
from src.config import salt
import datetime


class AuthProcessing:
    def __init__(self, engine):
        self.engine = engine

    @staticmethod
    def encrypt_string(hash_string):
        hash_string += salt
        sha_signature = hashlib.sha256(hash_string.encode()).hexdigest()
        return sha_signature

    def auth_user(self, login, hash):
        query = "SELECT id, type FROM users WHERE account='" + login + "' AND hash='" + hash + "';"

        print(query)
        with self.engine.connect() as con:
            rs = con.execute(query)

            for row in rs:
                print(row)
                self.create_session(row[0])

    def create_session(self, id):
        query = "INSERT INTO sessions (user, time, hash) VALUES ('" + str(id) + "', '" + datetime.datetime.now().isoformat(' ') + "', '123');"

        with self.engine.connect() as con:
            rs = con.execute(query)