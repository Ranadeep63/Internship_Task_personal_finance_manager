import json
import os
import hashlib

class UserAuth:
    def __init__(self, users_file="users.json"):
        self.users_file = users_file
        if not os.path.exists(self.users_file):
            with open(self.users_file, 'w') as f:
                json.dump({}, f)

    def _hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

    def register(self, username, password):
        with open(self.users_file, 'r') as f:
            users = json.load(f)

        if username in users:
            print("⚠️ Username already exists. Please choose another.")
            return False

        users[username] = self._hash_password(password)
        with open(self.users_file, 'w') as f:
            json.dump(users, f, indent=4)

        print("✅ Registration successful!")
        return True

    def login(self, username, password):
        with open(self.users_file, 'r') as f:
            users = json.load(f)

        hashed = self._hash_password(password)
        if username in users and users[username] == hashed:
            print(f"✅ Login successful! Welcome, {username}.")
            return True
        else:
            print("❌ Invalid username or password.")
            return False
