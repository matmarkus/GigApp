from sqlalchemy import Column, Integer, String, create_engine
import json
import os

users_data_file = 'users.json'

def load_users():
    """Loads users created in former sessions."""
    if os.path.exists(users_data_file):
        with open(users_data_file) as file:
            return json.load(file)
    return {}

def save_users(users):
    """Save users info for future sessions."""
    with open(users_data_file, 'w') as file:
        json.dump(users, file)

#"""dict for users, to be active during session."""
users = load_users()


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
        logged_in_user = username
        print(f"Logging succesfull. Welcome, {username}")
        return username
    else:
        print("Logging unsuccesfull. Please try again.")
        return login()

def show_logged_in_user():
    """FOR TESTING"""
    global logged_in_user
    if logged_in_user is None:
        print("Es gibt keine user.")
    else:
        print(f"Aktualnie zalogowany użytkownik: {logged_in_user}")



# def logout():
#
