from defs_users import register, login, show_logged_in_user
from sqlalchemy.orm import session
import config
import defs_gigs
from defs_gigs import add_gig, view_gigs, edit_gig, delete_gig

from defs_users import register, login, logout, show_logged_in_user

def menu():
    """Menu with 9 options."""
    while True:
        print("1. Register")
        print("2. Login")
        print("3. View Gigs")
        print("4. Add Gig")
        print("5. Edit Gig")
        print("6. Delete Gig")
        print("7. Logout")
        print("8. Exit")
        print("9. Show Logged In User")
        choice = input("Choose what you want to do: ")
        if choice == '1':
            register()
        elif choice == '2':
            if show_logged_in_user() is False:  # check if no user is logged in
                login()
            else:
                print("You are already logged in. Log out first if you want to switch account.")
        elif choice == '3':
            view_gigs()
        elif choice == '4':
            add_gig()
        elif choice == '5':
            edit_gig()
        elif choice == '6':
            delete_gig()
        elif choice == '7':
            logout()
        elif choice == '8':
            break
        elif choice == '9':
            show_logged_in_user()
        else:
            print("Invalid option. Please try again.")



