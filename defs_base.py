from defs_users import register, login
from sqlalchemy.orm import session
# from defs_gigs import


def menu():
    """Menu with 8 options."""
    while True:
        print("1. Register")
        print("2. Login")
        print("3. View Gigs")
        print("4. Add Gig")
        print("5. Edit Gig")
        print("6. Delete Gig")
        print("7. Logout")
        print("8. Exit")
        print("9. CHECKING THE CODE BUTTON.")
        choice = input("Choose what you want to do: ")
        if choice == '1':
            register()
            break
        elif choice == '2':
            login()
            break
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
            #TODO fix
            print("NARA")
        elif choice == '9':
            print(username)
        else:
            print("Invalid option. Please try again.")

