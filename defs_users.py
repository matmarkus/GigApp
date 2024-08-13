import json
import os
import config

users_data_file = 'users.json'

def load_users():
    """Loads users created in former sessions."""
    if os.path.exists(users_data_file):
        with open(users_data_file) as file:
            return json.load(file)
    return {}

users = load_users()

def save_users(users):
    """Save users info for future sessions."""
    with open(users_data_file, 'w') as file:
        json.dump(users, file)

def register():
    """Creating new user"""
    print("Creating your account.")
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if username in users:
        print("Username already exists. Please choose another name.")
        return register()
    else:
        users[username] = {'password': password}
        save_users(users)
        print("Registration successful!")

def login():
    """Login in"""
    global logged_in_user
    print("Login in your account.")
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if username in users and users[username]['password'] == password:
        config.logged_in_user = username
        print(f"Logging successful. Welcome, {username}.")
        return True
    else:
        print("Logging unsuccessful. Please try again.")
        return False

def show_logged_in_user():
    """Display the current logged-in user."""
    if config.logged_in_user is None:
        print("No user currently logged in.")
        return False
    else:
        print(f"Currently logged in user: {config.logged_in_user}")

def logout():
    global logged_in_user
    config.logged_in_user = None
    print("Logging out successful.")
