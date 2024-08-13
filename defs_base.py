def menu():
    while True:
        print("1. Register")
        print("2. Login")
        print("3. View Gigs")
        print("4. Add Gig")
        print("5. Edit Gig")
        print("6. Delete Gig")
        print("7. Logout")
        print("8. Exit")
        choice = input("Choose what you want to do: ")
    if choice == '1':
        register()
    elif choice == '2':
        login()
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
        #break daje 'break' outside loop error
        #TODO fix
        print("NARA")
    else:
        print("Invalid option. Please try again.")

if __name__ == '__main__':
    menu()

