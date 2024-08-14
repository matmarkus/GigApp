import config
from defs_gigs import view_gigs, add_gig, edit_gig, delete_gig, import_gigs_from_csv
from defs_users import register, load_users, login, logout
from ASCII import logo
from FAQ import documentation

load_users()

print(logo)
print("Welcome to GigApp - your place to manage concerts and festivals you've attended.")
print("Please login or register your account.")
def menu():
    while True:
        print("\nMain Menu")
        print("1. View Gigs - see your events.")
        print("2. Gigs Management - add, edit or delete.")
        print("3. User Management")
        print("4. About")
        print("5. Exit")

        choice = input("Choose a section: ")

        if choice == '1':
            view_gigs()
        elif choice == '2':
            gigs_management_menu()
        elif choice == '3':
            user_management_menu()
        elif choice == '4':
            print(documentation)
            menu()
        elif choice == '5':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")


def user_management_menu():
    """Submenu to choose options regarding user management."""
    while True:
        print("\nUser Management")
        if not config.logged_in_user:
            print("1. Register")
            print("2. Login")
            print("3. Go to Main Menu")
        else:
            print(f"Logged in as: {config.logged_in_user}")
            print("1. Logout")
            print("2. Back to Main Menu")

        choice = input("Choose an option: ")

        if not config.logged_in_user:
            if choice == '1':
                register()
            elif choice == '2':
                login()
            elif choice == '3':
                menu()
        else:
            if choice == '1':
                logout()
                menu()
            elif choice == '2':
                menu()
    else:
        print("Invalid option. Please try again.")


def gigs_management_menu():
    """Submenu to choose options regarding gigs in db."""
    while True:
        print("\nGigs Management")
        print("1. Edit Gigs")
        print("2. Add Gigs")
        print("3. Back to Main Menu")

        choice = input("Choose an option: ")

        if choice == '1':
            edit_gigs_menu()
        elif choice == '2':
            add_gigs_menu()
        elif choice == '3':
            menu()
        else:
            print("Invalid option. Please try again.")


def edit_gigs_menu():
    """Submenu to choose options regarding editing gigs in db."""
    while True:
        print("\nEdit Gigs")
        print("1. Edit Gig")
        print("2. Delete Gig")
        print("3. Back to Gigs Management")

        choice = input("Choose an option: ")

        if choice == '1':
            edit_gig()
        elif choice == '2':
            delete_gig()
        elif choice == '3':
            menu()
        else:
            print("Invalid option. Please try again.")


def add_gigs_menu():
    """Submenu to choose options regarding adding gigs to db."""
    while True:
        print("\nAdd Gigs")
        print("1. Add Gig Manually")
        print("2. Import Gigs from Last.fm")
        print("3. Back to Gigs Management")

        choice = input("Choose an option: ")

        if choice == '1':
            add_gig()
        elif choice == '2':
            file_path = input("""
                **CSV Creation Instructions**:
                1. Go to the website [https://mainstream.ghan.nl/export.html]
                2. Enter your username from Last.fm.
                3. Choose "Events (full)" from the options.
                4. Select CSV format and export the data.
                5. Ensure that the exported CSV file contains the following headers:
                   - artist
                   - date (format: YYYY-MM-DD)
                   - venue
                   - place (for city)
                   - country
                   - type (should be "festival" or not)
                   - title (name of the festival, if applicable)
                   - href (for comments)
                Please enter the path to the CSV file. 
                For example: C:\\Users\\Admin\\Desktop\\name_of_file.csv
                Path: """)

            import_gigs_from_csv(file_path)
        elif choice == '3':
            menu()
        else:
            print("Invalid option. Please try again.")


user_management_menu()
