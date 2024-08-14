import json
import os
import config
import getpass

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
    """Creates a new user account.

    This function prompts the user for a username and a password to create a new account.
    If the provided username already exists, the user is informed and prompted to choose another username.
    Once a valid username and password are provided, the new user is added to the `users` dictionary,
    and the data is saved.
    """
    print("Creating your account.")
    username = input("Enter your username: ")
    password = getpass.getpass(prompt="Enter your password: ") #hiding password

    if username in users:
        print("Username already exists. Please choose another name.")
        return register()
    else:
        users[username] = {'password': password}
        save_users(users)
        print("Registration successful!")


def login():
    """Logs a user into their account.

    If username exists in the users dict and password
    matches stored data, the user is logged in and it's saved
    to global variable 'logged_in_user'
    """
    global logged_in_user
    print("Login in your account.")
    username = input("Enter your username: ")
    password = getpass.getpass(prompt="Enter your password: ") #hiding password

    # Verify credentials
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
