import hashlib
import secrets
import string
from random import random

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
                return row[0], self.create_session(row[0])
            return 0, ""

    def create_session(self, id):
        secret = ''.join(secrets.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(256))
        hash_val = self.encrypt_string(secret)
        query = "INSERT INTO sessions (user, time, hash) VALUES ('" + str(id) + "', '" + datetime.datetime.now().isoformat(' ') + "', '" + hash_val + "');"

        with self.engine.connect() as con:
            con.execute(query)
        return hash_val

    def out(self, user, session):
        query = "UPDATE sessions SET actual=true WHERE user='" + user + "' AND hash = '" + session + "';"
        with self.engine.connect() as con:
            con.execute(query)