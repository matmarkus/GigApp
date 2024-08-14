import getpass
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

login()
