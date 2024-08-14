from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import Session
from defs_users import register, save_users, load_users, users, login, show_logged_in_user, logout
import json
import os
import config
from defs_gigs import view_gigs, add_gig, edit_gig, delete_gig, import_gigs_from_csv

load_users()


def menu():
    while True:
        print("\nMain Menu")
        print("1. User Management")
        print("2. View Gigs")
        print("3. Gigs Management")
        print("4. Exit")

        choice = input("Choose a section: ")

        if choice == '1':
            user_management_menu()
        elif choice == '2':
            view_gigs()
        elif choice == '3':
            gigs_management_menu()
        elif choice == '4':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")


def user_management_menu():
    while True:
        print("\nUser Management")
        if not config.logged_in_user:
            print("1. Register")
            print("2. Login")
            print("3. Back to Main Menu")
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
                break
        else:
            if choice == '1':
                logout()
            elif choice == '2':
                break
    else:
        print("Invalid option. Please try again.")


def gigs_management_menu():
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
            break
        else:
            print("Invalid option. Please try again.")


def edit_gigs_menu():
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
            break
        else:
            print("Invalid option. Please try again.")


def add_gigs_menu():
    while True:
        print("\nAdd Gigs")
        print("1. Add Gig Manually")
        print("2. Import Gigs from CSV")
        print("3. Back to Gigs Management")

        choice = input("Choose an option: ")

        if choice == '1':
            add_gig()
        elif choice == '2':
            file_path = input("Enter the path to the CSV file: ")
            import_gigs_from_csv(file_path)
        elif choice == '3':
            break
        else:
            print("Invalid option. Please try again.")


menu()
