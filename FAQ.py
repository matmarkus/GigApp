documentation = """
GigApp Documentation 
Project Title: GigApp
Participant: Mateusz Smolka
GigApp is a Python-based application designed to help users manage concerts and festivals they have attended. The application offers functionalities to add, edit, view, and delete gig entries, along with user account management features such as registration, login, and logout. 
External Imports and Their Usage 
•	Standard Library Imports 
- *csv*: To handle reading gig data from CSV files. 
- *datetime*: For date validation and manipulation. 
- *textwrap*: To format text output for comments in the console. 
- *os*: To check for the existence of the user data file. 
- *json*: For reading and writing user data to a JSON file. 
•	 External Libraries
- *getpass_asterisk.getpass_asterisk*: To securely prompt for passwords with asterisks masking the input. Note that due to this module, the application should be run in a terminal emulator for proper functionality. Popular getpass.getpass unfortunately doesn’t provide aterisks.
 - *pandas*: For handling dataframes and exporting gig data to Excel files. 
- *sqlalchemy*: To create and manage the SQLite database for storing gig data. 
Running the Application 
!!! To run the application, ensure you are using a terminal emulator due to the getpass_asterisk module requirement. This provides secure password input when registering or logging in. 
Database Management 
The application uses SQLAlchemy to manage an SQLite database for storing gig data. In case of any issues with the database, such as corrupted data or structural changes, the database file (gigs.db) should be deleted !!!, and the application should be restarted to allow it to recreate the database with the new schema. 
 Known Issues 
- *Database Problems*: If the database schema is edited, the existing database file must be deleted, and the application should be restarted to allow it to recreate the database with the new schema. 
- *Password Input*: The getpass_asterisk module requires the application to be run in a terminal emulator to mask password input correctly. 
 Additional Information
•	 Last.fm Integration Due to the lack of a suitable API from Last.fm, gig data must be scraped from the site. The application uses a script to import data from a CSV file exported from Last.fm via unofficial scraper  (https://mainstream.ghan.nl/export.html). If the Last.fm interface changes, the scraper may no longer function correctly, and adjustments may be required to maintain compatibility. 
•	 Duplicate Entries Prevention The application ensures that duplicate gig entries are not created. When adding or importing gigs, it checks for existing entries based on the artist, date, venue, city, and country to avoid duplicates.
•	  User-Specific Data Management Users must be logged in to add, view, edit, or delete gig entries. Each user's data is kept separate, ensuring that only the logged-in user's gigs are accessible and modifiable by that user. 
•	 Comprehensive Docstrings The functions within the application include detailed docstrings that explain their purpose, parameters, and workflows. These docstrings provide valuable information for understanding and maintaining the code. 
•	 About Section The details provided in this documentation are also available within the application under the "About" section in the main menu, offering users easy access to information about the application's functionalities and usage. 
•	For backups I’ve used GitHub.

 Project Structure 
•	 main.py The main script that initializes the application, displays the menu, and handles user navigation through different sections such as viewing gigs, managing gigs, and managing user accounts. 
•	 defs_gigs.py Contains functions related to gig management, including: - add_gig: Adds a new gig entry to the database. - view_gigs: Displays gig entries with optional filtering and sorting. - edit_gig: Edits an existing gig entry. - delete_gig: Deletes a selected gig entry. - import_gigs_from_csv: Imports gig data from a CSV file. - export_to_excel: Exports gig data to an Excel file. 
•	 defs_users.py Contains functions related to user management, including: - load_users: Loads user data from a JSON file. - save_users: Saves user data to a JSON file. - register: Registers a new user. - login: Logs in an existing user. - logout: Logs out the current user. - show_logged_in_user: Displays the currently logged-in user. 
•	 ASCII.py Contains the ASCII art logo of the application.  
•	config.py Contains a global variable logged_in_user to keep track of the currently logged-in user.  Without that code was generating problems.
 Menu Structure 
•	 Main Menu - *View Gigs*: Displays the user's gig entries. - *Gigs Management*: Submenu for adding, editing, or deleting gigs. - *User Management*: Submenu for registering, logging in, or logging out. - *About*: Displays information about the application. - *Exit*: Exits the application. 
•	 User Management Menu - *Register*: Creates a new user account. - *Login*: Logs into an existing user account. - *Logout*: Logs out the current user. - *Go to Main Menu*: Returns to the main menu. 
•	 Gigs Management Menu - *Edit Gigs*: Submenu for editing or deleting gigs. - *Add Gigs*: Submenu for adding gigs manually or importing from a CSV file. - *Back to Main Menu*: Returns to the main menu. 
•	 Edit Gigs Menu - *Edit Gig*: Edits an existing gig entry. - *Delete Gig*: Deletes a selected gig entry. - *Back to Gigs Management*: Returns to the gigs management menu. 
•	 Add Gigs Menu - *Add Gig Manually*: Prompts the user to enter gig details manually. - *Import Gigs from Last.fm*: Prompts the user to import gig data from a CSV file. - *Back to Gigs Management*: Returns to the gigs management menu. 


"""