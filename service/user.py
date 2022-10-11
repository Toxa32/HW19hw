import hashlib

from dao.user import UserDAO
from constants import PWD_HASH_SALT, PWD_HASH_ITERATIONS

class UserService:
    def __init__(self, dao: UserDAO):
        self.dao = dao

    def get_one(self, uid):
        return self.dao.get_user_by_id(uid)

    def get_all(self):
        return self.dao.get_all_users()

    def create(self, user_data):
        return self.dao.create_user(**user_data)

    def update(self, uid, user_data):

        return self.dao.edit_user_by_id(uid, **user_data)

    def delete(self, uid):
        self.dao.delete_user_by_id(uid)

    def get_hash(self, password, salt):
        return hashlib.pbkdf2_hmac(
            'sha256',
            password.encode('utf-8'),  # Convert the password to bytes
            PWD_HASH_SALT,
            PWD_HASH_ITERATIONS
        ).decode("utf-8", "ignore")
